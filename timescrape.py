import requests
from bs4 import BeautifulSoup

#times of places I want to read & page requests#
page = requests.get("https://24timezones.com/usa_time/il_cook/chicago.php")
#iri_page = requests.get("https://24timezones.com/world_directory/time_in_tehran.php")
#cst_page = requests.get("https://24timezones.com/world_directory/time_in_shanghai.php")

#data parse#
chi = BeautifulSoup(page.content, 'html.parser')
#iri = BeautifulSoup(iri_page.content, 'html.parser')
#cst = BeautifulSoup(cst_page.content, 'html.parser')

div_chi=chi.find(id="wt_leftCol")
#div_iri=iri.find(id="wt_leftCol")
#div_cst=cst.find(id="wt_leftCol")

chi_time=div_chi.find(id="currentTime").get_text()
#iri_time=div_iri.find(id="currentTime").get_text()
#cst_time=div_cst.find(id="currentTime").get_text()


#prints#
print("Chicago:",chi_time)
#print("Tehran:",iri_time)
#print("Shanghai:",cst_time)

