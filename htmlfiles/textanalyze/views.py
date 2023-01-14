from django.http import HttpResponse 
from django.shortcuts import render, HttpResponse
import scrapper as sc
def home(request):
    return render(request,'home.html')
    # return HttpResponse("ohi")
def articles(request):
    text = request.GET.get('text','default')
    print(text)
    
    req=5
    para=""
    hdm=""
    res_url=[]
    # que = input("Enter Keyword to find : ")
    que = text
    res_url=sc.goosearch(que,req,res_url)
    for i in range(len(res_url)):
        x=res_url[i]
        tree=sc.scraping(x)
        for hd in tree.find_all("h1"):
            hde=hd.text
            hdm+=hde
            print("\n HEAD - ", hde, "\n")
            print(x,"\n")
        for ra in tree.find_all("p"):
            para1=ra.text
            para+=para1
    concat_para=para.replace("\t", "")
    concat_para=concat_para.replace('.','.\n ')
    sc.fwrite(concat_para)
    for link in res_url:
        '''<div class="article"><a href="{{link}}"></a></div>")'''.appendTo(".articlecontainer")


 

    return render(request,'articles.html')



