import requests
from pprint import pprint

#Just for testing, I will use zipcode #
city = input('Enter your city : ')

#How the API is implemented
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=d420078c9fe54d5e0c8633f8699be0d9'.format(city)
res = requests.get(url)
data = res.json()

#Reading the data and doing some conversion
temp_C = data['main']['temp']
#K->C->F
temp_F_exact = ((temp_C-273)*1.8)+32
#Rounding Sif Figs
temp_F=round(temp_F_exact,1)
#Reads description like: sunny, cloudy, rain, etc. 
description = data['weather'][0]['description']

#Printing the info
print("Temperature:",temp_F,'F')
print("Report:",description)
