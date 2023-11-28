import telegram
import asyncio
import os
from crawler import get

bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
message_text = get()
processed_ids = set()

async def main():
    bot = telegram.Bot(bot_token)
    async with bot:
        updates = await bot.get_updates()

        for update in updates:
            user = update.message.chat
            user_id = user.id
            if user_id not in processed_ids:
                processed_ids.add(user_id)
                await bot.send_message(text=message_text, chat_id=user_id)


if __name__ == '__main__':
    asyncio.run(main())