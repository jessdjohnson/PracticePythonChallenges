# -*- coding: utf-8 -*-
"""
Challenge 19: Decode a webpage 2
For prompt, visit: https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

Goal: Use the BeautifulSoup and requests Python packages to print to screen the text of the article on
the following webpage: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
Split it up on 4 pages and make it easy to read without clicking any buttons.

Jess Johnson, 08/09/2019
"""
from bs4 import BeautifulSoup
import requests

  
if __name__ == '__main__':    
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    
    r_html = r.text
    
    soup = BeautifulSoup(r_html, "html.parser")
  
    all_p_cn_text_body = soup.select("div.grid--item.body.body__container.article__body.grid-layout__content > p")

    for elem in all_p_cn_text_body:
        print(elem.text)
  