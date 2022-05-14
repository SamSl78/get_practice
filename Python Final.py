import requests
import json
def weather_data(query):
   api_key = "a030b16c4423ac74d57ed503128c43fe"
   base_url = "https://openweathermap.org/appid"
   complete_url = base_url + "appid=" + api_key + "a030b16c4423ac74d57ed503128c43fe" + query
res=requests.get(complete_url);
return res.json();

def display_results(weathers,city):
  print("{}'s temperature: {}°F ".format(city,weathers['main']['temp']))
  print("Wind speed: {} m/s".format(weathers['wind']['speed']))
  print("Description: {}".format(weathers['weather'][0]['description']))
  print("Weather: {}".format(weathers['weather'][0]['main']))

def main():
  city=input('Enter the city:')
  print()

  try:
    query='q='+city;
    w_data=weather_data(query);
    display_results(w_data, city)
    print()
