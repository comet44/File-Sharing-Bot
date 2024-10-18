


import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=984847)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    addachemu_info = [] 
    if data == "adda_chem":
      addachemu_info = [
        f''' 🔮 **ADDA 24x7  2024 - 25 **

 
**🌱[NITESH DEVNANI ✘ MOLE CONCEPT ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NDU5Nzk5MDIzNjk1MTIwLTE1NDY5ODE4MzM2MDg4OTYw)**

**🌱[NITESH DEVNANI ✘ ATOMIC STRUCTURE ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NDcwODIwMjY3MzI4MzQ0LTE1NDgxODQxNTEwOTYxNTY4)**

**🌱[NITESH DEVNANI ✘ PERIODIC TABLE ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NDgyODQzNDQyMjAwOTUyLTE1NDg1ODQ5MjM1OTE5MTA0)**

**🌱[NITESH DEVNANI ✘ CHEMICAL BONDING ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NDg2ODUxMTY3MTU4NDg4LTE1NDk2ODcwNDc5NTUyMzI4)**

**🌱[NITESH DEVNANI ✘ THERMODYNAMICS ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NDk3ODcyNDEwNzkxNzEyLTE1NTA0ODg1OTI5NDY3NDAw)**

**🌱[NITESH DEVNANI ✘ EQUILLIBRIUM ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NTA1ODg3ODYwNzA2Nzg0LTE1NTE0OTA1MjQxODYxMjQw)**

**🌱[NITESH DEVNANI ✘ REDOX ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NTE1OTA3MTczMTAwNjI0LTE1NTE4OTEyOTY2ODE4Nzc2)**

**🌱[NITESH DEVNANI ✘ SOME BASIC CONCEPT OF ORGANIC CHEMISTRY ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NTE5OTE0ODk4MDU4MTYwLTE1NTMzOTQxOTM1NDA5NTM2)**

**🌱[NITESH DEVNANI ✘ HYDROCARBON ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NTM0OTQzODY2NjQ4OTIwLTE1NTM5OTUzNTIyODQ1ODQw)**

**🌱[NITESH DEVNANI ✘ P BLOCK ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NTQwOTU1NDU0MDg1MjI0LTE1NTQyOTU5MzE2NTYzOTky)**

**🌱[NITESH DEVNANI ✘ SOLUTION ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NTQzOTYxMjQ3ODAzMzc2LTE1NTQ3OTY4OTcyNzYwOTEy)**

**🌱[NITESH DEVNANI ✘ CHEMICAL KINETICS ](https://t.me/{BOT_USERNM}?start=Z2V0LTE1NTQ4OTcwOTA0MDAwMjk2LTE1NTUxOTc2Njk3NzE4NDQ4)**    ''',
                
    ]
    
    # Send each piece of information as a separate message
    for info in addachemu_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.1)

        await query.answer("ADDA 24x7 CHEMISTRY LECTURES SENT SUCESSFULLY✅", show_alert=True)
