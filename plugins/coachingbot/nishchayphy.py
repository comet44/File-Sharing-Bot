import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=1003)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    nishchayphy_info = [] 
    if data == "ny_phy":
      nishchayphy_info = [
        f''' 
🌱**[BASIC MATHS ✘ NISHCHAY 3.0 ](https://t.me/{BOT_USERNM}?start=Z2V0LTgxMjU2NjIzNTE0MDQyNDAtODEyNzY2NjIxMzg4MzAwOA)**

🌱**[MOTION ✘ NISHCHAY 3.0 ](https://t.me/{BOT_USERNM}?start=Z2V0LTgxMjg2NjgxNDUxMjIzOTItODEzNjY4MzU5NTAzNzQ2NA)**

🌱**[RELATIVE MOTION ✘ NISHCHAY 3.0](https://t.me/{BOT_USERNM}?start=Z2V0LTgxMzc2ODU1MjYyNzY4NDgtODEzODY4NzQ1NzUxNjIzMg)**

🌱**[MOTION IN 2D ✘ NISHCHAY 3.0 ](https://t.me/{BOT_USERNM}?start=Z2V0LTgxMzk2ODkzODg3NTU2MTYtODE0NDY5OTA0NDk1MjUzNg)**

🌱**[NLM ✘ NISHCHAY 3.0](https://t.me/{BOT_USERNM}?start=Z2V0LTgxNDU3MDA5NzYxOTE5MjAtODE0NzcwNDgzODY3MDY4OA)**

🌱**[FRICTION ✘ NISHCHAY 3.0 ](https://t.me/{BOT_USERNM}?start=Z2V0LTgxNDg3MDY3Njk5MTAwNzItODE1MDcxMDYzMjM4ODg0MA)**        ''',
                
        
              
        
    ]
    
    # Send each piece of information as a separate message
    for info in nishchayphy_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.5)

        await query.answer("LECTURES SENT SUCESSFULLY✅", show_alert=True)
    
        parse_mode=ParseMode.MARKDOWN,    
