import requests
from bs4 import BeautifulSoup

url = 'https://www.edu.tw/helpdreams/Grants.aspx?n=2BBF7170197CE7D3&sms=0A01A72AAB9E5CD4'


def get():
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    table = soup.find('table', id='ContentPlaceHolder1_gvIndex')
    items = table.find_all('a')
    req = ""

    for item in items:
        title = item.text
        addr = "https://www.edu.tw/helpdreams/" + item['href']
        req += title + '\n' + addr + '\n\n'

    return req