

import requests
from bs4 import BeautifulSoup
import pandas as pd
r=requests.get('https://urdu.geo.tv/trending/coronavirus')
# prints the first 1000 characters of 
# print(r.text[0:1000])
#  soup reading html and making sense of structure
soup=BeautifulSoup(r.text,'html.parser')
# return soup obj called result which have all the class with cstor
results=soup.find_all('div',attrs={'class':'col-xs-6 col-sm-6 col-lg-6 col-md-6 singleBlock'})

print(len(results))


first_result=results[0]
print(first_result.contents)
# print(first_result.find('a')['href']) #url
# print(first_result.find('span').text) #date
# print(first_result.find('h2').text) #detail
# print(first_result.find('div').text) #title
# print(first_result.find('a')['data-vr-contentbox']) #category
# categories = ['pakistan', 'world', 'sports', 'entertainment', 'business']



records=[]
for result in results:
    url=result.find('a')['href']
    time=result.find('span').text
    detail=result.find('h2').text
    title=result.find('div').text
    category=result.find('a')['data-vr-contentbox']
    records.append((title,time,category,detail,url))
print(records)
# print(records[0:5])

df=pd.DataFrame(records,columns=['title','time','category','detail','url'])
print(df.head())
print(df.tail())
df.to_csv('scrap.csv',index=True,encoding='utf-8-sig')
