import requests as req
from bs4 import BeautifulSoup as bs
url = "https://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnBuilding.do?mCode=MN202"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}
web = req.get(url, headers = headers)
def u_menu():
    soup = bs(web.content,'html5lib')
    menucard = soup.select('.menu-tbl')
    won = soup.select('.menu-tit01')
    menu = soup.select('h3.menu-tit01+p')
    day = soup.select('.day')
    date = soup.select('.date')
    # print(day,date)
    for d, dd, w, m in zip(day, date, won, menu):
        print('='*15)
        print(d.text,dd.text)
        print('='*15)
        print(w.text+'\n'+m.text)

if __name__ == '__main__':
    mel()