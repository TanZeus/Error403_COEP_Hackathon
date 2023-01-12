import requests
from bs4 import BeautifulSoup
import re
import os 
import pandas as pd

x=input("Enter URL : ")
r=requests.get(x)
para=""
tree = BeautifulSoup(r.content, 'html.parser')
good_html = tree.prettify()
for hd in tree.find_all("h1"):
    hde=hd.text
    print("HEAD - ", hde, "\n")
for ra in tree.find_all("p"):
    para1=ra.text
    para+=para1

concat_para=para.replace('.','.\n ')
print(concat_para)

f=open("Para_Swap.txt", "w")
f.write("Title\n")
f.write(concat_para)
f.close()

df = pd.read_csv('Para_Swap.txt', sep='\t')
df.to_csv('output.csv', index=False)
