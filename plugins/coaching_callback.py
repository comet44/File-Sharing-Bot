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


@Bot.on_callback_query(group=567)
async def hlpcallback(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "ch_cb":
        await query.message.edit_text(
            text = f''' SELECT YOUR SUBJECT ✅ ''',
            disable_web_page_preview = False,
            reply_markup = InlineKeyboardMarkup(
                [
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
  )
)
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
