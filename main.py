from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import pickle

from dataset.cinema_class import Cinema

title = "Joker"
date = "4/11/19"

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="drivers/chromedriver", options=chrome_options)

pack = []

with open("dataset/cinemas.p","rb") as log:
    pack = pack + pickle.load(log)

results = []
print("%s  ||  %s"%(title, date))
print("--------------------------------")

for p in pack:
    r = [p.name, p.search(driver,title,date)]
    try:
        print("%s:\n%s\n"%(r[0], r[1][0]))
    except:
        pass
