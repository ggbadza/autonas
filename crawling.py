import requests
from bs4 import BeautifulSoup
def nyaa_crawling(url):

    response = requests.get(url)
    log=open('errlog.txt', 'w')

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select('tr > td:nth-child(2)')
        magnet= soup.select('tr > td:nth-child(3) > a:nth-child(2)')
        torrlist={'number':[], 'title':[], 'magnet':[]}
        for i in range(len(title)):
            if str(title[i])[32:39].isdigit():
                log.write(str(title[i])[32:39])
                log.write(str(title[i].get_text()))
                torrlist['number'].append(str(title[i])[32:39])
                torrlist['title'].append(str(title[i].get_text()))
            else:
                log.write(str(title[i])[49:56])
                log.write(str(title[i].get_text())[3:])
                torrlist['number'].append(str(title[i])[49:56])
                torrlist['title'].append(str(title[i].get_text())[3:])
            
            log.write(str(magnet[i])[9:-40]+'\n\n')
            torrlist['magnet'].append(str(magnet[i])[9:-40])            
        log.close()
        return torrlist

    else : 
        return response.status_code
