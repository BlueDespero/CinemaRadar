import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from dataset.output_class import Output_class


def cinema_city_search(c_cinema, driver, title, date):
    def dated_url():
        date_object = datetime.strptime(date, '%d/%m/%y')
        url_1 = c_cinema.url.split("at=")[0]+"at="
        url_2 = "&"+"".join(c_cinema.url.split("at=")[1].split("&")[1:])
        d_url = str(url_1 +
        "%04d-%02d-%02d"%(date_object.year,date_object.month,date_object.day)
        + url_2)
        return d_url

    def prep_output(unprepared):
        splitted = unprepared[0].split("\n")
        itr = len(splitted)
        out = []
        for i in range(0,itr,3):
            out.append(Output_class(splitted[i], splitted[i+1], splitted[i+2]))
        return out
    
    url = dated_url()
    driver.get(url)
    results = []

    driver.find_element_by_xpath("/html/body/section[4]/section/div[1]/div/div[3]/div[3]/div/div/button").click()
    search_bar = driver.find_element_by_xpath("/html/body/div[9]/div[2]/div/div/input")
    search_bar.send_keys(str(title) + Keys.RETURN)
    content = driver.find_element_by_xpath("/html/body/section[4]/section/div[1]/section/div[2]/div/div/div/div[2]/div/div[2]").text
    results.append(content)
    return prep_output(results)


def multikino_search(c_cinema, driver, title, date):
    def dated_url():
        date_object = datetime.strptime(date, '%d/%m/%y')
        url_1 = c_cinema.url.split("=")[0]+"="
        d_url = str(url_1 +
        "%04d-%02d-%02d"%(date_object.year,date_object.month,date_object.day))
        date_today = datetime.today()
        clicks = date_object.day - date_today.day
        return d_url, date_object, clicks

    def prep_output(unprepared, date_obj):
        if unprepared == []:
            return unprepared

        splitter = ".%02d"%(date_obj.month)
        unprepared = [x.split(splitter)[1] for x in unprepared]

        splitted = unprepared[0].split("\n")[1:]
        itr = len(splitted)
        out = []
        for i in range(0,itr,2):
            t, l = splitted[i+1].split(',')
            out.append(Output_class(t, splitted[i],l))
        return out

    url, date_obj, clicks = dated_url()
    driver.get(url)

    time.sleep(5)
    try:
        driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    except:
        pass

    day_forward = driver.find_elements_by_class_name("timePicker_forw")
    for _ in range(clicks): 
        time.sleep(1)
        day_forward[0].click()

    results = []
    content = driver.find_elements_by_class_name("filmlist__item")
    for x in content:
        if title in x.text:
            try:
                x.find_element_by_class_name("filmlist__times--expand").click()
            except:
                pass

    content = driver.find_elements_by_class_name("filmlist__item")
    for x in content:
        if title in x.text:
            results.append(x.text)

    return prep_output(results, date_obj)


def kino_odra_search(c_cinema, driver, title, date):
    def dated():
        date_object = datetime.strptime(date, '%d/%m/%y')
        return date_object

    def prep_output(unprepared):
        if unprepared == []:
            return unprepared
        unprepared = unprepared[0].split('\n')[3:]
        results = []
        for i in range(0, len(unprepared), 3):
            hour = unprepared[i+1]
            t, l = unprepared[i+2].split(" ")
            results.append(Output_class(t, hour, l))
        return results

    date_obj = dated()
    date_s = "%02d-%02d-%04d"%(date_obj.day,date_obj.month,date_obj.year)

    driver.get(c_cinema.url)
    results = []
    content = driver.find_elements_by_class_name("page-repertoire-movie")
    content = [c for c in content if date_s in c.text]
    if content != []:
        content = [c for c in content[0].find_elements_by_class_name("movie-info-container") if title.upper() in c.text]
        if content!=[]: results.append(content[0].text)
    else:
        driver.get(c_cinema.url + "page/2/")
        content = driver.find_elements_by_class_name("page-repertoire-movie")
        content = [c for c in content if date_s in c.text][0]
        content = [c for c in content.find_elements_by_class_name("movie-info-container") if title.upper() in c.text]
        if content!=[]: results.append(content[0].text)

    return prep_output(results)


def go_kino_search(c_cinema, driver, title, date):
    def dated_url():
        date_object = datetime.strptime(date, '%d/%m/%y')
        url_1 = "/".join(c_cinema.url.split("/")[:-1])+"/"
        d_url = str(url_1 +
        "%02d-%02d-%04d"%(date_object.day,date_object.month,date_object.year))
        return d_url

    url = dated_url()
    print(url)
    driver.get(url)

    content = driver.find_element_by_tag_name("body")
    #for c in content: print(c.text)
    #content = [c for c in content if title.upper() in c.text]
    print(content.text)

searches_by_type = {
    'cinema city':cinema_city_search,
    'multikino':multikino_search,
    'kino odra':kino_odra_search,
    'go kino':go_kino_search
}