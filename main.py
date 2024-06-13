import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor

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

def get_chat_ids(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    chat_ids = set()

    if response.status_code == 200:
        updates = response.json().get('result', [])
        for update in updates:
            chat_id = update.get('message', {}).get('chat', {}).get('id')
            if chat_id:
                chat_ids.add(chat_id)
    else:
        print(f"Failed to get updates: {response.status_code} - {response.text}")
    
    return list(chat_ids)

def send_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to send message to {chat_id}: {response.status_code} - {response.text}")

def send_messages_concurrently(bot_token, chat_ids, messages):
    with ThreadPoolExecutor() as executor:
        futures = []
        for chat_id in chat_ids:
            for message in messages:
                futures.append(executor.submit(send_message, bot_token, chat_id, message))
        for future in futures:
            future.result()

if __name__ == '__main__':
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not bot_token:
        print("Error: TELEGRAM_BOT_TOKEN environment variable is not set.")
        exit(1)
    
    messages = get_grants()
    chat_ids = get_chat_ids(bot_token)
    if chat_ids:
        send_messages_concurrently(bot_token, chat_ids, messages)
    else:
        print("No chat IDs found.")