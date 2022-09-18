import configparser
from crawling import nyaa_crawling
from torrent import torrent_down


properties = configparser.ConfigParser()
properties.read('config.ini')

#if 'CONFIG' in properties:
#    config=properties["CONFIG"]
#else :
#    config={}
#config.setdefault('url','https://nyaa.si/?f=0&c=0_0&q=%5BSubsPlease%5D+%26+1080') #기본 url 설정
#properties.set("CONFIG", "url", config["url"])

if 'TORRENT' in properties:
    torrent=properties["TORRENT"]
else :
    torrent={}
torrent.setdefault('torrentlist',[])
torrent.setdefault('recent','0')
properties.set("TORRENT", "torrentlist", torrent["torrentlist"])
properties.set("TORRENT", "recent", torrent["recent"])

if 'ACCOUNT' in properties:
    account=properties["ACCOUNT"]
else :
    account={}

account.setdefault('id','admin')
account.setdefault('pw','djemals')
properties.set('ACCOUNT', "id", account["id"])
properties.set('ACCOUNT', "pw", account["pw"])

url=config['url']



with open('config.ini', "w") as f:
    properties.write(f)



torrentlist=nyaa_crawling(url)

print(torrentlist)

