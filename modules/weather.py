import requests
import json
import time


def weather(settings):

  api_key = settings['settings']['modules']['weather']['api_key']
  city = settings['foption']
  verbose_response = settings['soption']

  if city is None:
    city = settings['settings']['modules']['weather']['default_city']

  weather_request = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
      city + '&appid=' + api_key

  r = requests.get(weather_request)
  weather_info = r.json()

  if verbose_response == 'more':
    response = get_verbose_response(weather_info)
  else:
    response = get_regular_response(weather_info)

  print city.upper()
  print response


def get_regular_response(weather_info):
  temp = kelvin_to_celsius(weather_info['main']['temp'])
  sky = weather_info['weather'][0]['description']
  return 'Temp: ' + str(int(temp)) + 'C, ' + sky


def get_verbose_response(weather_info):
  temp = kelvin_to_celsius(weather_info['main']['temp'])
  max_temp = kelvin_to_celsius(weather_info['main']['temp_max'])
  min_temp = kelvin_to_celsius(weather_info['main']['temp_min'])

  sunrise_time = unix_to_human_hour(weather_info['sys']['sunrise'])
  sunset_time = unix_to_human_hour(weather_info['sys']['sunset'])

  sky = weather_info['weather'][0]['description']

  return 'Temp: ' + str(int(temp)) + 'C, ' + ' Max: ' + str(int(max_temp)) + 'C; Min: ' + str(int(min_temp)) + 'C, ' + sky + '\nSunrise: ' + sunrise_time + 'h\nSunset: ' + sunset_time + 'h'


def kelvin_to_celsius(kelvin):
  celsius = kelvin - 273.15
  return celsius


def unix_to_human_hour(unixstamp):
  return time.strftime("%H:%M", time.gmtime(unixstamp))
