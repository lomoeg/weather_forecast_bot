import telebot
import requests
import config

bot = telebot.TeleBot(config.telegram_bot_token)
city = 'Moscow'


def emoji(weather_desc):
    if weather_desc == "Rain":
        return "🌧"
    elif weather_desc == "Thunderstorm":
        return "⛈"
    elif weather_desc == "Snow":
        return "❄️"
    elif weather_desc == "Clear":
        return "☀️"
    elif weather_desc == "Clouds":
        return "☁️"
    elif weather_desc == "Tornado":
        return "🌪"
    else:
        return "🌫"


def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + config.weather_token
    rsp_data = requests.get(url).json()
    try:
        output_main = "📍{city} - " \
                      "{description} {emoji}\n\n" \
                      "Temperature: {temp} ‎°C\n" \
                      "Feels like: {feels_like} °C\n\n" \
                      "Pressure: {pressure} hPa\n" \
                      "Humidity: {humidity}%\n\n".format(description=str(rsp_data['weather'][0]['description']).title(),
                                                         temp=round(rsp_data['main']['temp']),
                                                         feels_like=round(rsp_data['main']['feels_like']),
                                                         pressure=rsp_data['main']['pressure'],
                                                         humidity=rsp_data['main']['humidity'],
                                                         city=city.title(),
                                                         emoji=emoji(rsp_data['weather'][0]['main']))
    except Exception as err:
        print("Error: " + str(err))
        output_main = "I can't get weather from the server. Please, try again."
        if rsp_data['cod'] == "404":
            output_main = "City was not found, sorry."
    wind_speed, wind_dir, output_recommendations = "", "", ""
    try:
        wind_speed = "Wind speed: {wind_speed} m/sec\n".format(wind_speed=rsp_data['wind']['speed'])
    except: pass

    # try:
    #     wind_dir = "Wind direction: {wind_dir} deg\n".format(wind_dir=rsp_data['wind']['deg'])
    # except: pass
    try:
        wind_dir = "Wind direction: {wind_dir} deg\n".format(wind_dir=rsp_data['wind']['deg'])
    except: pass

    try:
        output_recommendations = recommend_clothes(rsp_data['main']['temp'],
                                                   rsp_data['weather'][0]['main'],
                                                   rsp_data['wind']['speed'])
    except: pass
    output_main += wind_speed + wind_dir + output_recommendations
    return output_main


def recommend_clothes(temp, gen_descr, wind_speed):
    res = "\n-----"
    if temp > 20:
        res += "\nQuite warm. Well, today you will be irresistible in a shirt.\n"
    elif temp > 10:
        res += "\nGreat weather! Wear a sweatshirt.\n"
    elif temp > -10:
        res += "\nNot that warm. Wear a jacket/coat and everything will be fine.\n"
    else:
        res += "\nBrrrr.. Cold. Take a look at a down jacket.\n"

    if gen_descr == "Rain":
        res += "Don't forget an umbrella ☔\n️"
    if wind_speed > 5:
        res += "Also the wind is pretty strong. Wear windproof clothing."
    return res



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi there, {name}!\n\n I am the Smart Weather Bot.\n'
                                      'I can clarify the weather in your city.\n\n'
                                      'Just choose /getweather or enter the city'.format(name=message.from_user.first_name))


@bot.message_handler(commands=['getweather'])
def print_weather(message):
    msg = bot.send_message(message.chat.id, "Please, enter the city in English")
    bot.register_next_step_handler(msg, get_city_step)


@bot.message_handler(content_types=["text"])
def get_city_step(message):
    try:
        bot.send_message(message.chat.id, get_weather(message.text))
    except Exception as e:
        bot.reply_to(message, 'Some problems occured.')
        print(str(e))


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()


if __name__ == '__main__':
    bot.polling(none_stop=True)