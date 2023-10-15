import requests
import datetime as dt

api_key = 'eb36bd40e5b5bc10ca9a28261723522d'

user_input=input("enter city name: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?"
url= base_url+"appid="+api_key+"&q="+user_input

def kelvin_to_celsius(kelvin):
    celsius=kelvin-273.15
    return celsius

response= requests.get(url).json()

if response['cod']==200:
    
    temp_kelvin= response['main']['temp']
    temp_celcius=kelvin_to_celsius(temp_kelvin)
    description=response['weather'][0]['description']
    feelslike_kelvin=response['main']['feels_like']
    feelslike_celsius=kelvin_to_celsius(feelslike_kelvin)
    humidity=response['main']['humidity']
    sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
    sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])
    wind_speed=response['wind']['speed']

    print(f"Temperature in {user_input}: {temp_celcius:.2f} °C")
    print(f"Temperature in {user_input} feels like: {feelslike_celsius:.2f} °C")
    print(f"Humudity in {user_input}: {humidity} %")
    print(f"Wind Speed in {user_input}: {wind_speed} m/s")
    print(f"Weather Description {user_input}: {description} ")
    print(f"Sun Rise in {user_input} at: {sunrise_time} local time")
    print(f"Sun Set in {user_input} at: {sunset_time} local time")

else:
    if response['cod']=='404':
        message=response['message']
        print(message)









 