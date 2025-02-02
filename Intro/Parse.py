from bs4 import BeautifulSoup
import requests

##url = 'https://brokercheck.finra.org/individual/summary/2378311'
##url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
url='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
print(soup.find_all('title'))
print(soup.prettify())
