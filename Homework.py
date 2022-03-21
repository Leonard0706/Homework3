import requests 
from bs4 import BeautifulSoup
respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books")
soup = BeautifulSoup(respond.text, "html.parser")
lis = soup.find_all("li",class_="item")
for each_li in lis[:3]:
    img = each_li.find("img")
    imgSrc = img['src']
    bookName = img['alt']
    imgRespond = requests.get(imgSrc)
    print(imgRespond) #<Response [200]>
    print(imgRespond.content)
    with open(bookName+".jpg","bw") as file:
        file.write(imgRespond.content)

    