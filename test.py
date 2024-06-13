import requests
import os

def test_for_env():
    assert os.environ.get('TELEGRAM_BOT_TOKEN') is not None
    assert os.environ.get('USER_ID') is not None
    
def test_for_boardcast(bot_token, user_id):
    message = "Test for boardcast."
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={user_id}&text={message}"
    requests.get(url)