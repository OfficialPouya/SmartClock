#GUI
from bs4 import BeautifulSoup
from guizero import App
import requests

#times of places I want to read & page requests#
chi_page = requests.get("https://24timezones.com/usa_time/il_cook/chicago.php")


#data parse#
chi = BeautifulSoup(chi_page.content, 'html.parser')


div_chi=chi.find(id="wt_leftCol")


chi_time=div_chi.find(id="currentTime").get_text()





app = App(title="Smart Clock")
from guizero import App, Text
welcome_message = Text(app, text=chi_time, size=40, font="Times New Roman", color="blue")
app.display()
