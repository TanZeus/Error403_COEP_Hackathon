from time import sleep
import io
import requests
from bs4 import BeautifulSoup
import re
import os 
import pandas as pd
from googlesearch import search


#Define how many requests you want to send.


def goosearch(query,n,res_url):
    query += " site:news.google.com"
    sleep(1)
    qser = search(query, num_results=n)
    for url in qser:
        res_url.append(url)
    return res_url

def fwrite(cpa):
    f=io.open("newspara.txt", "w", encoding="UTF-8")
    f.truncate(0)
    f.write("Content\n")
    f.write(cpa)
    f.close()

def scraping(url):
    r=requests.get(url)
    tree = BeautifulSoup(r.content, 'html.parser')
    return tree


