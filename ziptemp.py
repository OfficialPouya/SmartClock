#zip -> direct weather#
import requests
import time
from bs4 import BeautifulSoup
from pprint import pprint
from selenium  import webdriver
#Input for ZipCode and Check


zip_code = input("Enter Your Zip Code: ")
# time_mode = 
while(len(zip_code)!=5):
	zip_code = input("Enter a VALID Zip Code: ")

page_url="https://www.zip-codes.com/zip-code/"+zip_code+"/zip-code-"+zip_code+".asp"
page = requests.get(page_url)
page_parse = BeautifulSoup(page.content, 'html.parser')

all_table = page_parse.find(class_="statTable")
name_table = all_table.find_all(class_="info")

table_tag= all_table.find_all(class_="label")
if(table_tag[9].get_text()=="Time Zone:"):
	time_zone = name_table[9].get_text()
elif(table_tag[10].get_text()=="Time Zone:"):
	time_zone = name_table[10].get_text()

city_name = name_table[1].get_text()
state_name = name_table[2].get_text()


def weather_get():
#How the API is implemented
	url = 'http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=d420078c9fe54d5e0c8633f8699be0d9'
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
	weather_print()	



def weather_print():
	#Printing the info
	# print(time_zone)
	print("Temperature:",temp_F,'F')
	print("Report:",description.capitalize())


def time_zone_time():
	if(time_zone=="Central (GMT -06:00)"):
		time_page = requests.get("https://24timezones.com/usa_time/il_cook/chicago.php")

	elif(time_zone=="Mountain (GMT -07:00)"):
		time_page = requests.get("https://24timezones.com/world_directory/time_in_denver.php")

	elif(time_zone=="Pacific (GMT -08:00)"):
		time_page = requests.get("https://24timezones.com/world_directory/time_in_los_angeles.php")

	elif(time_zone=="Alaska (GMT -09:00)"):
		time_page = requests.get("https://24timezones.com/world_directory/time_in_anchorage.php")

	elif(time_zone=="Hawaii-Aleutian Islands (GMT -10:00)"):
		time_page = requests.get("https://24timezones.com/world_directory/time_in_honolulu.php")

	elif(time_zone=="Eastern (GMT -05:00)"):
		time_page = requests.get("https://24timezones.com/world_directory/time_in_new_york.php")

	return(time_page)


def time_parse():
	time_zone_time();
	#data parse for time#
	time_data = BeautifulSoup(time_page.content, 'html.parser')
	time_col=time_data.find(id="wt_leftCol")
	online_time=time_col.find(id="currentTime").get_text()

	time_split=online_time.split()
	clock = time_split[0]
	ampm = time_split[1]
	day = time_split[2]
	month = time_split[4]
	year = time_split[5]
	day_num_string = time_split[3].split(',')
	print (clock)
	day_num=int(day_num_string[0])
	if(day_num%10==1):
		postfix="st,"
	elif(day_num%10==2):
		postfix="nd"
	elif(day_num%10==3):
		postfix="rd"
	else:
		postfix="th"

