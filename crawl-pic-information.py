#http://www.xiaohuar.com/list-1-0.html
import requests,time
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
num1=0
for i in range(0,7):
    a = requests.get("http://www.xiaohuar.com/list-1-%d.html"%i,headers = headers)
    a.encoding = 'gbk'
    a = etree.HTML(a.text)
    b = a.xpath("//div[@class ='img']")
    c1 = a.xpath("//em[@class = 'bold']/text()")
    num =0
    num1+=1
    list1 = []
    for i in b:
        a=i.xpath("./span/text()")
        b=i.xpath("./div/a/text()")
        c=i.xpath("./a/img/@src")
        c = "http://www.xiaohuar.com"+c[0]
        list1.append(c)
        img = requests.get(c, headers=headers, stream=True)
        print(c)
        with open("xiaohua.txt","a")as file1:
            file1.write(a[0]+b[0]+c+c1[num]+"\n")
        with open("./xiaohuapic/%s%s.jpg"%(b[0],a[0]),"wb") as file2:
            for j in img.iter_content(1024):
                file2.write(j)
        num+=1
    print(list1)
        # print("第%d页第%d个校花下载成功"%(num1,num))
##a.pop("searchFilter")
##b = a["list"]
##for i in b:
##    print("年龄："+str(i["age"])+"体重"+str(i["avoirdupois"])+"性别"+str(i["sex"])+"星座："+i['constellationName']+
##          "姓名："+i["nick"]+"身高"+str(i["stature"])+"城市"+i['cityName']+"学历"+i['degreeName']+"星座"+i[ 'constellationName'])
##    with open("./photo/%s"%i["nick"],"wb") as file:
##        url = i[ 'photoUri']
##        photo = requests.get(url,headers = headers,stream =True)
##        for i in photo.iter_content(1024):
##            file.write(i)

##http://www.xiaohuar.com
##/d/file/20191017/127c698a931462c55df8aa0ad65d208c.jpg
