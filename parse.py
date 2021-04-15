import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date
import error

#in: date(YYYY-MM-DD), dir id, group id
#out: list with shedule
def get_data(date_entry, id_dir=99, id_group=30687):
    if not error.date_valid(date_entry):
        return []
    year, month, day = map(int, date_entry.split('-'))
    p = date(year, month, day).weekday()
    url ='https://ruz.spbstu.ru/faculty/'+str(id_dir)+'/groups/'+str(id_group)+'/?date='+date_entry

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('li', class_='schedule__day')

    list = []
    items1 = items[p].find_all('li', class_='lesson')
    for k in items1:
        TimeAndLesson1 = k.find('div', class_='lesson__subject').text.strip()
        Teacher = k.find('div', class_='lesson__teachers').text.strip()
        Place = k.find('div', class_='lesson__places').text.strip()
        d =(TimeAndLesson1,Teacher, Place)
        list.append(d)
    return list
       

#print(get_data(input(' YYYY-MM-DD ')))
