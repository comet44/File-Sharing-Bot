


import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=9882)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    chemupw_info = [] 
    if data == "pw_chem":
      chemupw_info = [
        f'''  🔮 **CLASS 11 BIOLOGY PW CLASSROOM LECTURES**

🌱**[PERIODIC TABLE ✘ MOHIT SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTY4MTUxMzYyOTAyODk5NjgtNjgyMzE1MTc0MDIwNTA0MA)**

🌱**[CHEMICAL BONDING ✘ MOHIT SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTY4MjQxNTM2NzE0NDQ0MjQtNjgzOTE4MjY0MDAzNTE4NA)**

🌱**[COORDINATION COMPOUND ✘ MOHIT SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTY4NDAxODQ1NzEyNzQ1NjgtNjg0ODIwMDAyMTE4OTY0MA)**

🌱**[HYDROGEN ✘ MOHIT SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTY4NDkyMDE5NTI0MjkwMjQtNjg1MDIwMzg4MzY2ODQwOA)**

🌱**[S BLOCK ✘ MOHIT SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTY4NTEyMDU4MTQ5MDc3OTItNjg1MzIwOTY3NzM4NjU2MA)**

🌱**[P BLOCK  ✘ MOHIT SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTY4NTQyMTE2MDg2MjU5NDQtNjg2MzIyODk4OTc4MDQwMA)**

🌱**[D And F Block ✘ MOHIT SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTY4NjQyMzA5MjEwMTk3ODQtNjg2NTIzMjg1MjI1OTE2OA)**

🌱**[METALLURGY ✘ MOHIT SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTY4NjYyMzQ3ODM0OTg1NTItNjg2ODIzODY0NTk3NzMyMA)**

🌱**[ALL NOTES & DPP ✘ MOHIT SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTY4NjkyNDA1NzcyMTY3MDQtNjg3NzI1NjAyNzEzMTc3Ng)**        ''',
                
    ]
    
    # Send each piece of information as a separate message
    for info in chemupw_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.1)

        await query.answer("PW CHEMISTRY LECTURES SENT SUCESSFULLY✅", show_alert=True)
