import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date


date_entry = input('Введите данные в формате YYYY-MM-DD ')
year, month, day = map(int, date_entry.split('-'))
p = date(year, month, day).weekday()
print(p)
url ='https://ruz.spbstu.ru/faculty/99/groups/30687/?date='+date_entry
#'+str(year)+'-'+str(month)+'-'+str(day-p)
print(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('li', class_='schedule__day')



i = -1
for n in items:
    i = i+1
    if i is not p:
        continue
    print(i)
    
    items1 = n.find_all('li', class_='lesson')
    for k in items1:
        TimeAndLesson1 = k.find('div', class_='lesson__subject').text.strip()
        print(f'{TimeAndLesson1 }  ')
     
    #TimeAndLesson1 = i.find('div', class_='lesson__subject').text.strip()
    #TimeAndLesson2 = i.find('div', class_='lesson__subject').text.strip()
    #TimeAndLesson3 = i.find('div', class_='lesson__subject').text.strip()


    #print(f'{n}:  {TimeAndLesson1} и еще {TimeAndLesson2}  ')