

import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=1001)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    nishchaybio_info = [] 
    if data == "ny_bio":
      nishchaybio_info = [
        f''' 
🌱**[LIVING WORLD ✘ NISHCHAY  3.0 ](https://t.me/{BOT_USERNM}?start=Z2V0LTc5NzgzNzg0NTkyMTQ3OTItNzk3OTM4MDM5MDQ1NDE3Ng)**
                    
🌱**[BIOLOGICAL CLASSIFICATION ✘ NISHCHAY  3.0 ](https://t.me/{BOT_USERNM}?start=Z2V0LTgxMDg2Mjk1MjAzMzQ3MTItODExMTYzNTMxNDA1Mjg2NA)**

🌱**[EVOLUTION ✘ NISHCHAY  3.0  ](https://t.me/{BOT_USERNM}?start=Z2V0LTgxMTI2MzcyNDUyOTIyNDgtODExNjY0NDk3MDI0OTc4NA)**

🌱**[REPRODUCTIVE HEALTH ✘ NISHCHAY  3.0  ](https://t.me/{BOT_USERNM}?start=Z2V0LTgxMTc2NDY5MDE0ODkxNjgtODExNzY0NjkwMTQ4OTE2OA)**

🌱**[BIOMOLECULES ✘ NISHCHAY  3.0  ](https://t.me/{BOT_USERNM}?start=Z2V0LTgxMTg2NDg4MzI3Mjg1NTItODEyNDY2MDQyMDE2NDg1Ng)**

🌱**[MOLECULAR BASIS OF INHERITANCE ✘ NISHCHAY  3.0 ](https://t.me/{BOT_USERNM}?start=Z2V0LTg4ODgxMzIwMjQ1NzU0NjQtODg5MzE0MTY4MDc3MjM4NA)**        
        
        ''',
                
        
              
        
    ]
    
    # Send each piece of information as a separate message
    for info in nishchaybio_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.5)

        await query.answer("LECTURES SENT SUCESSFULLY✅", show_alert=True)
    
        parse_mode=ParseMode.MARKDOWN,
        
