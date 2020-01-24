import requests
from bs4 import BeautifulSoup
#Input for ZipCode and Check
zip_code = input("Enter Your Zip Code: ")
while(len(zip_code)!=5):
	zip_code = input("Enter a VALID Zip Code: ")
page_url="https://www.zip-codes.com/zip-code/"+zip_code+"/zip-code-"+zip_code+".asp"
page = requests.get(page_url)
page_parse = BeautifulSoup(page.content, 'html.parser')

all_table = page_parse.find(class_="statTable")
name_table = all_table.find_all(class_="info")
print(name_table[1].get_text())
print(name_table[2].get_text())
print(name_table[9].get_text())
