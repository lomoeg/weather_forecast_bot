# weather_forecast_bot

### Название задачи

Умный сервис прогноза погоды

### Уровень сложности 
Задача со звездочкой

### Язык программирования и технологии
- Python 3.6
- telebot / Telegram Bot API
- OpenWeather API

#### Пользовательский интерфейс
Чат-бот в Telegram

### Формат ответа
Данные, полученные через API с сервера подставляются в шаблон ниже. {Recommendations} формируется исходя из параметров 
- {temp}
- {wind_speed}
- 'main' field from API response
```
📍{city} - {description} {emoji}
Temperature: {temp} °C
Feels like: {feels_like} °C
Pressure: {pressure} hPa
Humidity: {humidity}%

Wind speed: {wind_speed} m/sec
Wind direction: {wind_dir} deg

-----
{Recommendations}
```

