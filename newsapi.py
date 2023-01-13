# importing requests package
import requests	
import json
def NewsFromBBC():
	
	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "a650d5a7df3746418f25a4ae2ba725ce"
	}
	main_url = " https://newsapi.org/v2/everything?q=tesla&apiKey=a650d5a7df3746418f25a4ae2ba725ce"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()
    
	# getting all articles in a string article
	article = open_bbc_page["articles"]
    # obj = json.loads(article)
	# empty list which will
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["content"])
		
	for i in range(len(results)):
		
		# printing all trending news
		print(i + 1, results[i])

	# #to read the news out loud for us
	# from win32com.client import Dispatch
	# speak = Dispatch("SAPI.Spvoice")
	# speak.Speak(results)				

# Driver Code
if __name__ == '__main__':
	
	# function call
	NewsFromBBC()
