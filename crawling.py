import requests
from bs4 import BeautifulSoup

url = 'https://nyaa.si/?f=0&c=0_0&q=%5BSubsPlease%5D+%26+1080'

response = requests.get(url)

log=open('errlog.txt', 'w')

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('tr > td:nth-child(2)')
    magnet= soup.select('tr > td:nth-child(3) > a:nth-child(2)')
    for i in range(len(title)):
        log.write(str(title[i])[32:39])
        log.write(str(title[i].get_text()))
        log.write(str(magnet[i])[9:-40]+'\n\n')
    log.close()

else : 
    print(response.status_code)