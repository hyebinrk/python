
import requests as req
url = "https://finance.naver.com/sise/sise_market_sum.naver"
web = req.get(url)
html = web.text
f1 = html.find("삼성전자")
html[f1:f1+100].find('<td class="number">')
where = html[f1:f1+100].find('<td class="number">')
print('삼성전자 : '+html[f1:f1+100][where:50].replace('<td class="number">',"").replace('</td>',"").replace("
","")+"원")
