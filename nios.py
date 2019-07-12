from bs4 import BeautifulSoup
from time import sleep
import csv
import re
# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("/home/akashrao96/chromedriver_linux64/chromedriver") # if you want to use chrome, replace Firefox()    with Chrome()
driver.get("https://sdmis.nios.ac.in/registration/locate-study-center")
sleep(1)
search_exeute = driver.find_element_by_xpath("//*[@name='button']").submit()
sleep(20)
src = driver.page_source # gets the html source of the page
parser = BeautifulSoup(src,'html.parser') # initialize the parser and parse the source "s)
sleep(1)
f = open('nios_data.csv', 'w')
div = parser.find("div",{"class": "studycenter__main-content fullwidth"})
list_of_rows = []
for row in div.find_all('div',{"class" : "studycenter__main-content--tile"}):
    list_of_cells = []
    for cell in row.find_all('div',{"class":"ai-data"}):
        text = cell.text.replace("&nbsp;", "")
        list_of_cells.append(text)
    for col in row.find_all('div',{"class":"ai-address"}):
        text = col.text
        mob = re.findall(r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",text)
        email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text)
        list_of_cells.append(email)
        list_of_cells.append(mob)
    list_of_rows.append(list_of_cells)
    writer=csv.writer(f)
    writer.writerow(list_of_cells)
    print (list_of_rows)
f.close()
driver.close()
