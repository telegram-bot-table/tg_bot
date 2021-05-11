import requests
from bs4 import BeautifulSoup
import csv

url = 'https://ruz.spbstu.ru/faculty/101/groups'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
items1 = soup.find_all('a', class_='groups-list__link', href=True)

list = []

for k in items1:
    T = k.text.strip()
    A = (''.join(i for i in k['href'] if i.isdigit()))
    A = A[2:]
    list.append([T, A])
    print(T + ',' + A)


##########################################################################
# FILENAME = "ги.csv"
#
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(list)
##########################################################################

# print(get_data(input(' YYYY-MM-DD ')))
