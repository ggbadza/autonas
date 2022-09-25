import configparser
from crawling import nyaa_crawling
from torrent import torrent_down
import csv


properties = configparser.ConfigParser()
properties.read('config.ini')

if 'CONFIG' in properties:
    config=properties["CONFIG"]
else :
    properties.add_section("CONFIG")
    config={}
config.setdefault('recent','0')
#config.setdefault('url',r"https://nyaa.si/?f=0&c=0_0&q=%5BSubsPlease%5D+%26+1080") #기본 url 설정
#properties.set("CONFIG", "url", config["url"])
url='https://nyaa.si/?f=0&c=0_0&q=%5BSubsPlease%5D+%26+1080'


#if 'TORRENT' in properties:
#    torrentp=properties["TORRENT"]
#else :
#    properties.add_section("TORRENT")
#    torrentp={}

#torrent.setdefault('torrentlist',[])
#properties.set("TORRENT", "torrentlist", torrent["torrentlist"])


if 'ACCOUNT' in properties:
    account=properties["ACCOUNT"]
else :
    properties.add_section('ACCOUNT')
    account={}

account.setdefault('id','admin')
account.setdefault('pw','djemals')


#url=config['url']





#####################토렌트 파일 로드

csvf=open('torrent.csv', 'r', encoding='euc-kr')
csvfread=csv.reader(csvf)   
torrentdic={}
for row in csvfread:
    torrentdic[row[0][:10]]=row[1] # 0번에 제목, 1번에 저장할 주소

print(torrentdic)


torrentlist=nyaa_crawling(url)

for i in range(len(torrentlist['number'])):
    if torrentlist['number'][i]<=config['recent']:
        break
    if torrentlist['title'][i][14:24] in torrentdic:
        print(torrentlist['title'][i][14:24])##테스트
        torrent_down(account['id'],account['pw'],torrentlist['magnet'][i],torrentdic[torrentlist['title'][i][14:24]])

config['recent']=torrentlist['number'][0]

#### 설정파일 저장
properties.set("CONFIG", "recent", config["recent"])
properties.set('ACCOUNT', "id", account["id"])
properties.set('ACCOUNT', "pw", account["pw"])

with open('config.ini', "w") as f:
    properties.write(f)