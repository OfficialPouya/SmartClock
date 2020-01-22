import requests
from bs4 import BeautifulSoup
#insert your locations area for NOAH using your ZIP CODE#
#Main Page: weather.gov#
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.1538&lon=-87.9663#.Xic4W2hKiUk")
soup = BeautifulSoup(page.content, 'html.parser')


#This part of the code is used to read current temp and condition#
curr_day_body = soup.find(id="current-conditions-body")
curr_sum = soup.find(id="current_conditions-summary")
curr_cond = curr_sum.find(class_="myforecast-current").get_text()
curr_temp = curr_sum.find(class_="myforecast-current-lrg").get_text()

#This part of the code is used to read future Highs and Lows#
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")

today = forecast_items[0]
later_today = forecast_items[1]
tmw = forecast_items[2]
tmw_night = forecast_items[3]

#scrapes the text#
period=today.find(class_="period-name").get_text()
short_desc = today.find(class_="short-desc").get_text()
today_high = today.find(class_="temp").get_text()
today_low = later_today.find(class_="temp").get_text()
tmw_high = tmw.find(class_="temp").get_text()
tmw_low  = tmw_night.find(class_="temp").get_text()

#printing data#
print("Currently it is",curr_cond,"@",curr_temp)
print("Today's",today_high,today_low)
print("Tomorrow's",tmw_high,tmw_low)


