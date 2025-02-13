import requests as req
import sys
url = "https://finance.naver.com/sise/sise_market_sum.naver"
web = req.get(url)
html = web.text

arg = sys.argv
print(args[1])
def sam(jong = (args[1] or  '삼성전자'):
    f1 = html.find(jong)
    where = html[f1:f1+100].find('<td class="number">')
    return(f'{jong}: '+html[f1:f1+100][where:50].replace('<td class="number">',"").replace('</td>',"").replace("\n","")+"원")
    
if __name__=='__main__':
    print(sam)