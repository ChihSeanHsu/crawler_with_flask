# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:31:38 2019

@author: Sean
"""
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen



class MyWebCrawler:
    def __call__(self, web, web_encoding='utf-8'):
        res = requests.get(web)
        res.encoding = web_encoding
        self.soup = BeautifulSoup(res.text, 'html.parser') 
        
    def find_target(self, tag, *args, **kwargs):
        content = self.soup.find_all(tag, *args, **kwargs)
        return [title.text for title in content]

            

