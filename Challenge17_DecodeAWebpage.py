# -*- coding: utf-8 -*-
"""
Challenge 17: Decode a webpage
For prompt, visit: https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

Goal: Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

NOTE: The html schema has changed since thing challenge got posted....class = 'story-heading' doesn't exist
anymore.  The article titles are not in class = "css-STUFF" where STUFF is a string 
of randomly generated characters and changes for every article.  As such...I couldn't figure
out how to complete this exercise.  :-/  Will revisit later when I've played with HTML more.

Jess Johnson, 08/09/2019
"""
from bs4 import BeautifulSoup
import requests

  
if __name__ == '__main__':    
    url = 'https://www.nytimes.com/'
    r = requests.get(url)    
    r_html = r.text
    
    soup = BeautifulSoup(r_html, "html.parser")
    #print(soup.prettify())
    
    #all_p_cn_text_body = soup.find_all("div.gcss-189d5rw.e6b6cmu0 > h2")
    all_p_cn_text_body = soup.find_all("div > h2")
    

    print(all_p_cn_text_body)
    for elem in all_p_cn_text_body:
        print(elem.text)
    #site-content > div.css-189d5rw.e6b6cmu0 > div.css-19tmjl7 > section.css-jkpw0r > div > div:nth-child(1) > section > div > div.css-vxam5e > div:nth-child(2) > article > div > div > div:nth-child(1) > div > a > div > h2
    '''
    for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
    '''