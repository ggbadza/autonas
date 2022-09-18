from crawling import nyaa_crawling
from torrent import torrent_down

url = 'https://nyaa.si/?f=0&c=0_0&q=%5BSubsPlease%5D+%26+1080'

torrentlist=nyaa_crawling(url)