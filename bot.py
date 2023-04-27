import asyncio
from config import *
from telethon import TelegramClient,events

async def main():
    bot = await TelegramClient('session',API_ID,API_HASH).start()
    bot_taken=BOT_TOKEN
    
    async with bot:
        print("Logged in")
        @bot.on(events.NewMessage())
        async def handle_messsage(event):
         if event.message.message=='good morning':
           await event.reply("gd mrng")
            
            
        await bot.run_until_disconnected()
             
asyncio.run(main())
    
 
