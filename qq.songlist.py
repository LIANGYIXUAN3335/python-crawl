import requests,json
import random
import pandas as pd
def get_album_mid():
    url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI8198055058479126&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singerAlbum%22%3A%7B%22method%22%3A%22get_singer_album%22%2C%22param%22%3A%7B%22singermid%22%3A%22000aHmbL2aPXWH%22%2C%22order%22%3A%22time%22%2C%22begin%22%3A0%2C%22num%22%3A5%2C%22exstatus%22%3A1%7D%2C%22module%22%3A%22music.web_singer_info_svr%22%7D%7D"
    headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
             "referer"  :"https://y.qq.com/n/yqq/toplist/26.html"
        }
    r=requests.get(url,headers=headers)
    song_dict=r.json()
    # print(song_dict)
    album_info=[]
    for once in song_dict["singerAlbum"]['data']['list']:
        one_album_mid = once['album_mid']
        # song_mid(one_album_mid)
        album_name=once["album_name"]
        album_info.append({"one_album_mid":one_album_mid,"album_name":album_name})
    return album_info






def song_mid(album_info):
    for once in album_info:
        one_album_mid=once["one_album_mid"]
        url="https://c.y.qq.com/v8/fcg-bin/fcg_v8_album_info_cp.fcg?ct=24&albummid="+one_album_mid+"&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0"
        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "referer": "https://y.qq.com/n/yqq/toplist/26.html"
        }
        r = requests.get(url, headers=headers)
        song_dict = r.json()
        # print(song_dict)
        song_info=[]
        for once in song_dict["data"]["list"]:
            songmid =once["songmid"]
            songname=once["songname"]
            song_info.append({"songmid ":songmid ,
                             "songname":songname})
        return song_info
a=get_album_mid()
c=song_mid(a)
# print(c)
# print(a)
song_list=[]
for i in a:
    k=i["album_name"]
    song_list.append(k)

print(song_list)
# df=pd.DataFrame(d)
# df.to_csv("./songmid_info.txt",sep=",",header=None,index=None)