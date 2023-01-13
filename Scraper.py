from time import sleep
import io
import requests
from bs4 import BeautifulSoup
import re
import os 
import pandas as pd
from googlesearch import search


res_url=[]
para=""
que = input("Enter Keyword to find : ")
def goosearch(query):
    query += " site:news.google.com"
    sleep(3)
    qser = search(query, num_results=10)
    for url in qser:
        res_url.append(url)
        
goosearch(que)
for i in range(len(res_url)):
    x=res_url[i]
    r=requests.get(x)
    tree = BeautifulSoup(r.content, 'html.parser')
    good_html = tree.prettify()
    for hd in tree.find_all("h1"):
        hde=hd.text
        print("HEADD - ", hde, "\n")
    for ra in tree.find_all("p"):
        para1=ra.text
        para+=para1

concat_para=para.replace('.','.\n ')
print(concat_para)

f=io.open("Para_Swap.txt", "w", encoding="UTF-8")
f.write("Title\n")
f.write(concat_para)
f.close()

