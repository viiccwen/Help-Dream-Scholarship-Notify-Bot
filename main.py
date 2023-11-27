import telegram
import asyncio
import os
from crawler import get

bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
user_id = os.environ.get('USER_ID')

async def main():
    bot = telegram.Bot(bot_token)
    async with bot:
       await bot.send_message(text=get(), chat_id=user_id)

if __name__ == '__main__':
    asyncio.run(main())