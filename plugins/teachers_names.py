import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from pyrogram.enums import ParseMode
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages


@Bot.on_callback_query(group=1111)
async def hlpcallback(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "teamp1":
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» `Master Pro 1`

🌀 **Full Name »»** `Abhinav Batch for NEET 2024`
⚜️ **Start At:** 14 Jun, 2023""",
            reply_markup=InlineKeyboardMarkup(
        [
     [
        InlineKeyboardButton(text="Insaf Ali", callback_data="teajanmp1_1"),
        InlineKeyboardButton(text="Sikander Singh", callback_data="teafebmp1_1"),
    ],
    [
        InlineKeyboardButton(text="Aashish Bansal", callback_data="teamarmp1_1"),
        InlineKeyboardButton(text="Ajit Chandra Divedi (ACID Sir)", callback_data="teaaprmp1_1"),
    ],
    [
        InlineKeyboardButton(text="Ashish Gupta", callback_data="teamaymp1_1"),
        InlineKeyboardButton(text="Triyogi Mishra", callback_data="teajunmp1_1"),
    ],
    [
        InlineKeyboardButton(text="Jagdeep Singh", callback_data="teajulmp1_1"),
        InlineKeyboardButton(text="Manish Kumar Sharma", callback_data="teaaugmp1_1"),
    ],
    [
        InlineKeyboardButton(text="Piyush Gupta", callback_data="teaseptmp1_1"),
        InlineKeyboardButton(text="Parvez Khan", callback_data="teaoctmp1_1"),
    ],
    [
        InlineKeyboardButton(text="Parvez Babar", callback_data="teanovmp1_1"),
        InlineKeyboardButton(text="Sharad Mathur", callback_data="teadecmp1_1"),
    ],
        ],
        ),
   parse_mode=ParseMode.MARKDOWN,         
        )
