import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=100388372)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    crashup_info = [] 
    if data == "crashup":
      crashup_info = [
        f'''🌀 ** CRASHUP PHYSICS CRASH COURSE **

🌱**[PART 01 ](https://t.me/{BOT_USERNM}?start=Z2V0LTEwNTk0NDIwOTI1MjQ2NDE2LTEwNjM1NTAwMTA2MDYxMTYw)**

🌱**[PART 02 ](https://t.me/{BOT_USERNM}?start=Z2V0LTEwNjM2NTAyMDM3MzAwNTQ0LTEwNjgwNTg3MDExODMzNDQw)**

🌱**[PART 03 ](https://t.me/{BOT_USERNM}?start=Z2V0LTEwNjgxNTg4OTQzMDcyODI0LTEwNzEzNjUwNzQyNzMzMTEy)**
        ''',
                
        
              
        
    ]
    
    # Send each piece of information as a separate message
    for info in crashup_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.5)

        await query.answer("LECTURES SENT SUCESSFULLY✅", show_alert=True)
    
        parse_mode=ParseMode.MARKDOWN,
        
