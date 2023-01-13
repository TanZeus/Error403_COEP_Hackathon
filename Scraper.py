from time import sleep
import io
import requests
from bs4 import BeautifulSoup
import re
import os 
import pandas as pd
from googlesearch import search


#Define how many requests you want to send.
req=5
para=""
res_url=[]
que = input("Enter Keyword to find : ")

def goosearch(query,n):
    query += " site:news.google.com"
    sleep(1)
    qser = search(query, num_results=n)
    for url in qser:
        res_url.append(url)
    return res_url

def fwrite(cpa):
    f=io.open("newspara.txt", "w", encoding="UTF-8")
    f.write("Content\n")
    f.write(cpa)
    f.close()

def scraping(url):
    r=requests.get(x)
    tree = BeautifulSoup(r.content, 'html.parser')
    return tree


res_url=goosearch(que,req)
for i in range(len(res_url)):
    x=res_url[i]
    tree=scraping(x)
    for hd in tree.find_all("h1"):
        hde=hd.text
        print("\n HEAD - ", hde, "\n")
    for ra in tree.find_all("p"):
        para1=ra.text
        para+=para1
        print("Content - ", para1)
concat_para=para.replace('.','.\n ')
fwrite(concat_para)
