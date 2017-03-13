from bs4 import BeautifulSoup
import requests
from termcolor import colored
import sys
dict = {'TEEN': '/teen/horoscope-teen-weekly', 'LOVE': '/love/horoscope-love-daily-today', 'CAREER': '/career/horoscope-career-daily-today', 'MONEY': '/money/horoscope-money-weekly', 'FOOD': '/food/horoscope-food-weekly', 'HEALTH': '/wellness/horoscope-wellness-daily-today', 'SUN SIGN': '/general/horoscope-general-daily-today', 'PET': '/pet/horoscope-pet-weekly'}

for i in range(0,len(dict)):
  CATEGORIES = dict.items()[i][0]
  URL = dict.items()[i][1]
  print colored(CATEGORIES, 'green')

  r = requests.get("http://www.horoscope.com/us/horoscopes/love/horoscope-love-daily-today.aspx?sign=2")
  r = requests.get("http://www.horoscope.com/us/horoscopes"+URL+".aspx?sign=2")
  data = r.text
  soup = BeautifulSoup(data,"lxml")
  for tag in soup.p('b'):
    tag.replaceWith('')
  print soup.p.text
  print " "
