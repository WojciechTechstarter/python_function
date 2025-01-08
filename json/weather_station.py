import requests


# Example from the lesson

# response = requests.get("https://wttr.in/berlin?format=j1")
# daten = response.json()
# # jetzt sind die json daten in der variable daten gespeichert
# # print(daten)
# # print(daten["current_condition"][0]["temp_C"])
# temperatur = daten["current_condition"][0]["temp_C"]
# wetter = daten["current_condition"][0]["weatherDesc"][0]["value"]
# print(wetter)
# print(f"The weather in Berlin is {wetter} with {temperatur}°C")


##########   Aufgabe 2    ###################

###wrong aproach
#response = requests.get('https://wttr.in/warsaw?format=j1')
#data = response.json()





def f_location():
    location = input('Choose a city to check its temerature, perceived temperature and weather station: ')

    url = f'https://wttr.in/{location}?format=j1'
    response = requests.get(url)
    data = response.json()

    temperature = data['current_condition'][0]['temp_C']
    percived_temperature = data['current_condition'][0]['FeelsLikeC']
    weather_station = data['nearest_area'][0]['areaName'][0]['value']

    print(f'\n In {location} the temperature is equal to {temperature}°C,\n perceived temperature is equal to {percived_temperature}°C\n and the weather station of {location} is in {weather_station}')
    

f_location()