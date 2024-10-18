
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=338)
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "ch_chem":
        await query.message.edit_text(
            text = f''' 🌀 >**CLICK ON WHATEVER YOU WANT**
📍 **SUBJECT **: `CHEMISTRY `            
            ''',
            disable_web_page_preview = True,
            parse_mode = ParseMode.MARKDOWN,
            reply_markup = InlineKeyboardMarkup(
                [
                           
                    [
                      InlineKeyboardButton(text="UNACADEMY", callback_data="un_chem"),
                      InlineKeyboardButton(text="ALLEN CLASSROOM", callback_data="aln_chem"),
                      
                   ],
                   [
                     InlineKeyboardButton(text="PHYSICSWALLAH", callback_data="pw_chem"),
                     InlineKeyboardButton(text="ANAND MANI", callback_data="ny_chem"),
                   ],
                   [
                     InlineKeyboardButton(text="ADDA 24x7", callback_data="adda_chem"),
                   ], 
                   [
                    InlineKeyboardButton(text="👨🏻‍💻 BACK ", callback_data="ch_cb")
                   ],
                ],
            )
        )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
