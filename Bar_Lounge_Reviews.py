import requests
from bs4 import BeautifulSoup
import csv

pages = [0,10,20,30,40,50,60,70,80,90,100]

filename = open('bar_lounge.csv', 'w')
f = csv.writer(filename)
header = ['Name', 'Location', 'Reviews']
f.writerow(header)

for page in pages:
     req = requests.get('https://www.yelp.com/biz/bar-karaoke-lounge-toronto?start={}'.format(page))
     soup = BeautifulSoup(req.content,'html.parser')
     list_items = soup.find_all(class_="review__373c0__13kpL border-color--default__373c0__3-ifU")


     for i in list_items:
            name = i.find(class_='css-166la90').get_text()
            location = i.find(class_='css-n6i4z7').get_text()
            reviews = i.find(class_='raw__373c0__3rcx7').get_text()
            f.writerow([name, location, reviews])

filename.close()


