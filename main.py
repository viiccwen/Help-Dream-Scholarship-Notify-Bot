import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_grants():
    url = 'https://www.edu.tw/helpdreams/Grants.aspx?n=2BBF7170197CE7D3&sms=0A01A72AAB9E5CD4'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    table = soup.find('table', id='ContentPlaceHolder1_gvIndex')
    items = table.find_all('a')
    req = []

    for item in items:
        title = item.text
        addr = quote("https://www.edu.tw/helpdreams/" + item['href'])
        req.append(f"{title}\n{addr}")

    return req

def send_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to send message to {chat_id}: {response.status_code} - {response.text}")

def send_messages(bot_token, boardcast_chat_id, messages):
    for message in messages:
        send_message(bot_token, boardcast_chat_id, message)

if __name__ == '__main__':
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    boardcast_chat_id = os.environ.get('TELEGRAM_BOARDCAST_CHAT_ID')
    if not bot_token:
        print("Error: TELEGRAM_BOT_TOKEN environment variable is not set.")
        exit(1)
    
    messages = get_grants()
    send_messages(bot_token, boardcast_chat_id, messages)