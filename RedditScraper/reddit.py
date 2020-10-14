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


posts = []
upvotes = []
comments = []



postsFeed = driver.find_elements_by_css_selector("div.rpBJOHq2PR60pnwJlUyP0")

postsHeader = driver.find_elements_by_css_selector('._eYtD2XCVieq6emjKBH3m')

upvotesNumbers = driver.find_elements_by_css_selector("._1rZYMD_4xY3gRcSS3p8ODO")

commentsNumbers = driver.find_elements_by_css_selector(".FHCV02u6Cp2zYL0fhQPsO")





total_height = int(driver.execute_script("return document.body.scrollHeight"))

for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
    for feed in postsFeed:
        for header in postsHeader:
            posts.append(header.text)
        for upvote in upvotesNumbers:
            upvotes.append(upvote.text)
        for comment in commentsNumbers:
            comments.append(comment.text)
        
        


uniquePosts = []
for post in posts:
    if post not in uniquePosts:
        uniquePosts.append(post)


uniqueVotes = []
for vote in upvotes:
    if vote not in uniqueVotes:
        uniqueVotes.append(vote)


uniqueComments = []
for comm in comments:
    if comm not in uniqueComments:
        uniqueComments.append(comm)


postSeries = pd.Series(uniquePosts, name='POSTS')
upvoteSeries = pd.Series(uniqueVotes, name='UPVOTES')
commentSeries = pd.Series(uniqueComments, name='COMMENTS')



redditDf = pd.concat([postSeries, upvoteSeries, commentSeries], axis=1)

redditDf.to_csv('frontPage.csv', encoding='utf-8', index=False)






