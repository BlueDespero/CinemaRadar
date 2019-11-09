from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import pickle

from dataset.cinema_class import Cinema

def print_outputs(r):
    name, outs = r
    print("-- %s --"%(name))
    if outs == []:
        print("\t/No results/")

    while outs!=[]:
        curr = []
        a = outs[0]
        curr.append(a)
        for o in outs[1:]:
            if o.type == a.type and o.language == a.language:
                curr.append(o)

        for c in curr:
            outs.remove(c)

        print("\t%s  |  %s"%(a.type,a.language))
        hour = ""
        for c in curr:
            hour+= c.hours + " "
        print("\t%s"%hour)


title = input("What movie you want to check?\n\t")
date = input("What date are you interested in? (format dd/mm/yy)\n\t")


chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path="drivers/chromedriver", options=chrome_options)

pack = []

with open("dataset/cinemas.p","rb") as log:
    pack = pack + pickle.load(log)

print('\n')
for p in pack:
    r = [p.name, p.search(driver,title,date)]
    print_outputs(r)