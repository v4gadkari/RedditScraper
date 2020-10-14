from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
sys.path.insert(0,'/usr/local/bin/chromedriver')
import pandas as pd 
import numpy as np 




driver = webdriver.Chrome('chromedriver')

driver.get("https://www.reddit.com/")

time.sleep(10)

nearYouCommsList = []
nearYou = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/a[1]")
nearYou.click()
time.sleep(10)
nearYouComms = driver.find_elements_by_css_selector(".UGHNtX0DV78XSU_nT_p_l")
nearYouCommsDivs = driver.find_elements_by_css_selector("div._2mHuuvyV9doV3zwbZPtIPG")
nearYouHeight = int(driver.execute_script("return document.body.scrollHeight"))

for a in range(1, nearYouHeight, 5):
    driver.execute_script("window.scrollTo(0, {});".format(a))
    for comms in nearYouComms:
        for divs in nearYouCommsDivs:
            nearYouNames = divs.find_elements_by_css_selector("._3A9bf_kZ6VBA2VBRND5gvf")
            for name in nearYouNames:
                nearYouCommsList.append(name.text)
    

    

driver.execute_script("window.history.go(-1)")

time.sleep(20)

sportsList= []
sports = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/a[2]")
sports.click()
time.sleep(10)
sportsComms = driver.find_elements_by_css_selector(".UGHNtX0DV78XSU_nT_p_l")
sportsCommsDivs = driver.find_elements_by_css_selector("div._2mHuuvyV9doV3zwbZPtIPG")
sports_height = int(driver.execute_script("return document.body.scrollHeight"))

for i in range(1, sports_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
    for sportsComm in sportsComms:
        for sportsDivs in sportsCommsDivs:
            sportsNames = sportsDivs.find_elements_by_css_selector("._3A9bf_kZ6VBA2VBRND5gvf")
            for names in sportsNames:
                sportsList.append(names.text)



driver.execute_script("window.history.go(-1)")
time.sleep(20)


newsList = []
news = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/a[3]")
news.click()
time.sleep(10)
newsComms = driver.find_elements_by_css_selector(".UGHNtX0DV78XSU_nT_p_l")
newsCommDivs = driver.find_elements_by_css_selector("div._2mHuuvyV9doV3zwbZPtIPG")
news_height = int(driver.execute_script("return document.body.scrollHeight"))

for j in range(1, news_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(j))
    for newsComm in newsComms:
        for newsDivs in newsCommDivs:
            newsNames = newsDivs.find_elements_by_css_selector("._3A9bf_kZ6VBA2VBRND5gvf")
            for newsName in newsNames:
                newsList.append(newsName.text)



            


driver.execute_script("window.history.go(-1)")

time.sleep(20)


awwList = []
aww = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/a[4]")
aww.click()
time.sleep(10)
awwComs = driver.find_elements_by_css_selector(".UGHNtX0DV78XSU_nT_p_l")
awwComsDivs = driver.find_elements_by_css_selector("div._2mHuuvyV9doV3zwbZPtIPG")
aww_height = int(driver.execute_script("return document.body.scrollHeight"))

for k in range(1, aww_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(k))
    for awwCom in awwComs:
        for awwDiv in awwComsDivs:
            awwNames = awwDiv.find_elements_by_css_selector("._3A9bf_kZ6VBA2VBRND5gvf")
            for awwName in awwNames:
                awwList.append(awwName.text)



driver.execute_script("window.history.go(-1)")

time.sleep(20)



uniqueSportsComms = []
for word in sportsList:
    if word not in uniqueSportsComms:
        uniqueSportsComms.append(word)


uniqueLocalComms = []
for place in nearYouCommsList:
    if place not in uniqueLocalComms:
        uniqueLocalComms.append(place)



uniqueNewsComms = []
for article in newsList:
    if article not in uniqueNewsComms:
        uniqueNewsComms.append(article)

uniqueAwwComms = []
for aww in awwList:
    if aww not in uniqueAwwComms:
        uniqueAwwComms.append(aww)



localSeries = pd.Series(uniqueLocalComms, name="Button 1")
sportSeries = pd.Series(uniqueSportsComms, name="Button 2")
newSeries = pd.Series(uniqueNewsComms, name="Button 3")
awwSeries = pd.Series(uniqueAwwComms, name="Button 4")

otherCommunitiesDf = pd.concat([localSeries, sportSeries, newSeries, awwSeries], axis=1)
otherCommunitiesDf.to_csv('otherCommunities.csv', encoding='utf-8', index=False)



