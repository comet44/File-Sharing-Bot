import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID


@Bot.on_message(filters.command('lects') & filters.private, group=234)
async def help(bot: Bot, message: Message):
 buttons = [
        [
            InlineKeyboardButton("AKM SIR",   callback_data= "help_akm"),
            InlineKeyboardButton("AG SIR ",   callback_data= "help_ath"),
            InlineKeyboardButton("DR AG SIR ", callback_data= "help_dr"),
        ],
        [
            
            InlineKeyboardButton("YSY SIR", callback_data= "help_ysy"),
            InlineKeyboardButton("AB SIR", callback_data= "help_ab"),
            InlineKeyboardButton("RS SIR", callback_data= "help_rs"),
        ],
        [
           InlineKeyboardButton("ACID SIR", callback_data= "help_acid"),
           InlineKeyboardButton("IA SIR ", callback_data= "help_ia"), 
           InlineKeyboardButton("RD SIR ", callback_data= "help_rd"),
        ],
         [
            InlineKeyboardButton("ST SIR ", callback_data= "help_st"),
            InlineKeyboardButton("JS SIR ", callback_data= "help_js"), 
            InlineKeyboardButton("TNM SIR ", callback_data= "help_tnm"),
        ],
         [
            InlineKeyboardButton("SKC SIR ", callback_data= "help_skc"),
            InlineKeyboardButton("AKG SIR ", callback_data= "help_anu"), 
            InlineKeyboardButton("PB SIR  ", callback_data= "help_pb"),
         ],
  
    ]
 await message.reply_text( text = f'''Hey there... I'm Unacademy Lectures Bot  <a href = https://telegra.ph/file/00314693350157a35db7c.jpg >  </a> \n ✨I have  Unacademy Lectures ''',
   reply_markup = InlineKeyboardMarkup(buttons),                       
   disable_web_page_preview = False
   )
