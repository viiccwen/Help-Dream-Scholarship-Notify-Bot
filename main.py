import requests
import os
from bs4 import BeautifulSoup

def get():
    url = 'https://www.edu.tw/helpdreams/Grants.aspx?n=2BBF7170197CE7D3&sms=0A01A72AAB9E5CD4'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    table = soup.find('table', id='ContentPlaceHolder1_gvIndex')
    items = table.find_all('a')
    req = []

    for item in items:
        title = item.text
        addr = "https://www.edu.tw/helpdreams/" + item['href']
        addr = addr.replace('&', '\\&')

        req.append(title + '\n' + addr)

    return req
            
if __name__ == '__main__':
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    user_id = os.environ.get('USER_ID')
    messages = get()
    for message in messages:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={user_id}&text={message}"
        requests.get(url)