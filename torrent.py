from qbittorrent import Client

def torrent_down(id,pw,magnet,path):
    ub=Client("http://127.0.0.1:8080/")
    ub.login(id,pw)
    ub.download_from_link(magnet,savepath=path)