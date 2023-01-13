import requests
from bs4 import BeautifulSoup
import re
import os 
import pandas as pd
from googlesearch import search


res_url=[]
que = input("Enter Keyword to find : ")
def goosearch(query):
  query += " site:news.google.com"
  for url in search(query):
    res_url.append(url)

x=input("Enter URL : ")
r=requests.get(x)
para=""
tree = BeautifulSoup(r.content, 'html.parser')
good_html = tree.prettify()
for hd in tree.find_all("h1"):
    hde=hd.text
    print("HEADD - ", hde, "\n")
for ra in tree.find_all("p"):
    para1=ra.text
    para+=para1

concat_para=para.replace(',','|')
concat_para=concat_para.replace('.',',')
print(concat_para)

f=open("Para_Swap.txt", "w")
f.write(concat_para)
f.close()
