
import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from config import ADMINS
from bot import Bot

from helper_func import subscribed, encode, decode, get_messages

SB_IMAGE = "https://te.legra.ph/file/b28ea39afdd624a2b6f88.jpg"


@Bot.on_message(filters.command("list") & filters.user(ADMINS), group=87884)
async def stream_start(_: Client, message: Message):
    keyboard = [
        [
            InlineKeyboardButton("GET LIST ", callback_data="list_ioc"),
          
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_photo( photo = SB_IMAGE,
        caption = """ Click Button to get list 
        """,
        reply_markup=reply_markup
    )
