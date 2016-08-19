from pprint import pprint
import requests
import json

def weather(settings):

	api_key = settings['settings']['modules']['weather']['api_key']

	if settings['foption'] is None:
		city = settings['settings']['modules']['weather']['default_city']
	else:
		city = settings['foption']

	weather_request = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key

	r = requests.get(weather_request)
	weather_info = r.json()

	temp = kelvin_to_celsius(weather_info['main']['temp'])
	sky = weather_info['weather'][0]['description']

	print city.upper()
	print 'temp: ' + str(int(temp)) + ' degrees, ' + sky

def kelvin_to_celsius(kelvin):
	celsius = kelvin - 273.15
	return celsius