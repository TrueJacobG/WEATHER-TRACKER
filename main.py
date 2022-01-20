import sys
import requests


def display(weather_type, description, temp, temp_feels, pressure, humidity, wind):
    print(f"{weather_type} - {description}")
    print(f"Temperature: {int(temp)}°C Feeling: {int(temp_feels)}°C")
    print(f"Pressure: {pressure}hPa")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {int(wind)}km/h")


def weather():
    API_KEY = ""
    URL = "http://api.openweathermap.org/data/2.5/weather"

    if len(sys.argv) == 1:
        print("You have to add city as the flag")
        return False

    request = f"{URL}?appid={API_KEY}&q={sys.argv[1]}"
    respond = requests.get(request)

    if respond.status_code == 200:
        data = respond.json()

        weather_type = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"] - 273.15
        temp_feels = data["main"]["feels_like"] - 273.15
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"] * 3.6

        display(weather_type, description, temp, temp_feels, pressure, humidity, wind)

    else:
        print("Connection error")
        return False


def main():
    weather()


if "__main__" == __name__:
    main()
