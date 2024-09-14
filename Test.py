import aiohttp
import asyncio
from telegram import Bot
from telegram.error import TelegramError

# Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = '7302329685:AAGHcRCK4W7Qxk4zi1pyFdP0omUdete3IgQ'
CHAT_ID = '-1002141335528'

async def fetch_data():
    url = "https://lust.scathach.id/xhamster/search?key=milfs"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                resp.raise_for_status()
                json_data = await resp.json()
                return json_data
        except aiohttp.ClientError as e:
            print(f"HTTP error: {e}")
        except asyncio.TimeoutError:
            print("Request timed out")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

async def send_to_telegram(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except TelegramError as e:
        print(f"Telegram error: {e}")

async def main():
    data = await fetch_data()
    if data:
        # Convert data to a string or format it as needed
        message = str(data)  # Or format as needed
        await send_to_telegram(message)

if __name__ == "__main__":
    asyncio.run(main())
