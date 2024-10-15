import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=1002)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    nishchaychem_info = [] 
    if data == "ny_chem":
      nishchaychem_info = [
        f''' 
🌱**[MOLE CONCEPT ✘ NISHCHAY  3.0 ](https://t.me//{BOT_USERNM}?start=Z2V0LTgxNTE3MTI1NjM2MjgyMjQtODE1NDcxODM1NzM0NjM3Ng)**

🌱**[STRUCTURE OF ATOM  ✘ NISHCHAY  3.0](https://t.me//{BOT_USERNM}?start=Z2V0LTgxNTU3MjAyODg1ODU3NjAtODE1OTcyODAxMzU0MzI5Ng)**

🌱**[Classification OF ELEMENTS ✘ NISHCHAY  3.0 ](https://t.me//{BOT_USERNM}?start=Z2V0LTgxNjA3Mjk5NDQ3ODI2ODAtODE2NDczNzY2OTc0MDIxNg)**

🌱**[CHEMICAL BONDING  ✘ NISHCHAY  3.0](https://t.me//{BOT_USERNM}?start=Z2V0LTgxNjU3Mzk2MDA5Nzk2MDAtODE2OTc0NzMyNTkzNzEzNg)**

🌱**[THERMODYNAMICS ✘ NISHCHAY  3.0 ](https://t.me//{BOT_USERNM}?start=Z2V0LTgxNzA3NDkyNTcxNzY1MjAtODE3NDc1Njk4MjEzNDA1Ng)** ''',
                
        
              
        
    ]
    
    # Send each piece of information as a separate message
    for info in nishchaychem_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.5)

        await query.answer("LECTURES SENT SUCESSFULLY✅", show_alert=True)
    
        parse_mode=ParseMode.MARKDOWN,
