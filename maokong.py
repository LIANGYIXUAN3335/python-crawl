import requests, time, pymysql,re,os,numpy
from lxml import etree
import pandas as pd
#获取第一页中的电影名,电影
def get_page_info():
    url = "https://www.amazon.com/stores/page/462539A0-4246-4DA8-9283-DE56ED9E2D13?ingress=0&visitId=771864a3-1e02-487c-a6d4-5d03c8c2e875&ref_=ast_bln"
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    r = requests.get(url, headers=headers)
    html = etree.HTML(r.text)
    all_li = html.xpath("//div[@class='a-row stores-row stores-widget-btf']")
    print(all_li.text)
get_page_info()
    film_Info = []
    for once_li in all_li:
        title_name = once_li.xpath("./div[@class='channel-detail movie-item-title']/@title")
        id=once_li.xpath("./div[@class='channel-detail movie-item-title'] /a/@data-val")[0]
        moive_id=str(re.compile("{movieId:(.*?)}").findall(id)[0])
        film_Info.append({"moive_id":moive_id,"title_name":title_name})

   # print(film_Info)
    return film_Info

### 获得每个电影名称
##
def get_each_film(film_Info):
    each_film=[]
    for once in film_Info:
        c=int(once["moive_id"])
        url="https://maoyan.com/films/"+str(c)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Referer":"https://maoyan.com/films/1216383"}
        r = requests.get(url, headers=headers)
        html = etree.HTML(r.text)
        one_moive_info = html.xpath("//div[@class='banner']")
        for once in one_moive_info:
            moive_name=once.xpath(".//div [@class='movie-brief-container']/h3/text()")
            moive_name_time=once.xpath('.//div [@class="celeInfo-right clearfix"]//li[2]/text()')[0]
            moive_area=moive_name_time.split("/")[0].strip()
            moive_time=moive_name_time.split("/")[1].strip()
            picture_url=str(once.xpath("//div[ @class='avatar-shadow']/img[@class='avatar']/@src")[0])
            # print(type(picture_url))
            each_film.append({"moive_name":moive_name,"moive_time":'%s'%(moive_time),
            "moive_area":moive_area,"picture_url":picture_url})
    return each_film

def download_picture(each_film):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        basepath="./maoyan/"
        nowNum = 0
        if os.path.exists(basepath):
            pass
        else:
            os.mkdir(basepath)
       for once in each_film :
            a=once["picture_url"]
            img_r=requests.get(a,headers=headers,stream=True)
            savename=a.split("/")[-1]
            with open(basepath+"/"+savename+".jpg",'wb') as file:
                for j in img_r.iter_content(10240):
                    file.write(j)
            nowNum+=1
            print("第%d张图片下载成功"%(nowNum))


c=get_page_info()
d=get_each_film(c)
 download_picture(d)
df=pd.DataFrame(d)
df.to_csv("./movie_info.txt",sep=",",header=None,index=None)















