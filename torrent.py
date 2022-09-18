from qbittorrent import Client

def torrent_down(magnet,path):
    ub=Client("http://127.0.0.1:8080/")
    ub.login("admin","djemals")
    ub.download_from_link(magnet,savepath=path)