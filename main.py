import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import quote
from test import test_for_env, test_for_boardcast

def get_grants():    
    url = 'https://www.edu.tw/helpdreams/Grants.aspx?n=2BBF7170197CE7D3&sms=0A01A72AAB9E5CD4'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    table = soup.find('table', id='ContentPlaceHolder1_gvIndex')
    items = table.find_all('a')
    req = []

    for item in items:
        title = item.text
        addr =  quote("https://www.edu.tw/helpdreams/" + item['href'])

        req.append(title + '\n' + addr)

    return req
            
def get_chat_ids(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    chat_ids = set()

    if response.status_code == 200:
        updates = response.json().get('result', [])
        for update in updates:
            chat_id = update.get('message', {}).get('chat', {}).get('id')
            if chat_id:
                print(f"{chat_id}\n")
                chat_ids.add(chat_id)
    else:
        print('Failed to get chat ids.')
    
    return list(chat_ids)

def send_messages(bot_token, chat_ids, messages):
    for chat_id in chat_ids:
        for message in messages:
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(url)
            
if __name__ == '__main__':
    test_for_env()
    
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')

    messages = get_grants()
    
    chat_ids = get_chat_ids(bot_token)
    
    send_messages(bot_token, chat_ids, messages)