import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM , PICS




@Bot.on_message(filters.command('lectures') , group=334)
async def help(bot: Bot, message: Message):
 btn = [
        [
            InlineKeyboardButton("PHYSICS",   callback_data= "ch_phy"),
        ],
        [
         InlineKeyboardButton("CHEMSITRY ",   callback_data= "ch_chem"),
        ],
        [
            InlineKeyboardButton("BIOLOGY", callback_data= "ch_bio"),
        ],
        [
            InlineKeyboardButton("🔙BACK", callback_data= "start_cb"),
        ],
        
        
 ]
 
 await message.reply_photo(PICS , caption  = f''' 🔮 SELECT YOUR SUBJECT ''',
   reply_markup = InlineKeyboardMarkup(btn),                                  
   parse_mode=ParseMode.HTML ,
    )
