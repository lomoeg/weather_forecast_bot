# weather_forecast_bot

## Общее

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


## Формат ответа
Данные, полученные через API с сервера подставляются в шаблон ниже. {Recommendations} формируется исходя из параметров 
- {temp}
- {wind_speed}
- 'main' field from API response
```
📍{city}, {country} - {description} {emoji}
Temperature: {temp} °C
Feels like: {feels_like} °C
Pressure: {pressure} hPa
Humidity: {humidity}%

Wind speed: {wind_speed} m/sec
Wind direction: {wind_dir} deg

-----
{Recommendations}
```


## Демонстрация работы сервиса

Видео с обзором бота доступно [по ссылке](https://youtu.be/V7XCCo94pC4).

## Процесс работы программы

1. Данные от пользователя приходят через интерфейс мессенджера (Формат ввода: название города)
2. Исходя из полученных данных формируется API-запрос на сервер для получения погодных данных
3. Полученные данные обрабатываются 
4. Полученные данные отправляются пользователю

Все сообщения об ошибках выводятся в терминал.

## Как запустить программу

1. Выполните команду

``` git clone https://github.com/lomoeg/weather_forecast_bot ```

2. Откройте файл config.py и введите токены для работы с ботом и с погодным сервером
3. В терминале выполните команду
``` python3 bot.py ```
