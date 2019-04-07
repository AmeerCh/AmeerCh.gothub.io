     
## importing bs4, requests, fake_useragent and csv modules
import bs4
import requests
#import UserAgent
import csv
## create an array with URLs

year=20001  
for year in range(year,20850):
  urls = ['http://www.nhl.com/scores/htmlreports/20102011/GS0'+str(year)+'.HTM']

## initializing the UserAgent object
#user_agent = UserAgent()

## starting the loop

  for url in urls:
## getting the reponse from the page using get method of requests module
    page = requests.get(url)

## storing the content of the page in a variable
    html = page.content

## creating BeautifulSoup object
    soup = bs4.BeautifulSoup(html, "html.parser")

    heads=soup.findAll('table', { "id" : "StdHeader" })

## Then parse the HTML, extract any data
## write it to a file
    print(heads)
    with open("page2.csv",'wb') as f:
      f.write(page.content)
        #writer.writerow(heads)
#print(var)

        #var=var + 1
#print(var)

