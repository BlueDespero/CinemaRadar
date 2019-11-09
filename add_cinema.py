from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import time
import pickle

from dataset.cinema_class import Cinema

url1 = "https://www.cinema-city.pl/kina/wroclavia/1097#/buy-tickets-by-cinema?in-cinema=1097&at=2019-11-02&view-mode=list"
url3 = "https://multikino.pl/repertuar/wroclaw-pasaz-grunwaldzki/teraz-gramy/alfabetyczny?data=04-11-2019"
url2 = "https://www.cinema-city.pl/kina/korona/1067#/buy-tickets-by-cinema?in-cinema=1067&at=2019-11-03&view-mode=list"
url4 = "http://kultura.olawa.pl/kino/repertuar/"
url5 = "https://gokino.pl/olawa/repertuar/03-11-2019"

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="drivers/chromedriver", options=chrome_options)


cin1 = Cinema("Wrocław", "Wroclavia", url1, "cinema city")
cin2 = Cinema("Wrocław", "Korona", url2, "cinema city")
cin3 = Cinema("Wrocław", "Pasaż Grunwaldzki", url3, "multikino")
cin4 = Cinema("Oława", "Kino Odra", url4, "kino odra")

pack = [cin1,cin2,cin3,cin4]
try:
    with open("dataset/cinemas.p","rb") as log:
        pack = pack + pickle.load(log)
except:
    pass

with open("dataset/cinemas.p","wb") as log:
    pickle.dump(pack,log)

'''
cin5 = Cinema("Oława", url5, "go kino")
cin5.search(driver,title,date)
'''