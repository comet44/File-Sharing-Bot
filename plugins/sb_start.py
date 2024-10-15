
import random
import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from .buttons import fsub_button, start_button
from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT,BOT_USERNM,PICS
from helper_func import  encode, decode, get_messages , subscribed
from database.database import add_user, del_user, full_userbase, present_user
SB_IMAGE = "https://te.legra.ph/file/85f5929ef3f4e7e0a41bc.jpg"





@Bot.on_message(filters.command("unabatches"), group=2006)
async def stream_start(_: Client, message: Message):
    keyboard = [
        [
            InlineKeyboardButton("Master Pro 1", callback_data="mp_1"),
            InlineKeyboardButton("Master Pro 2", callback_data="mp_2"),
        ],
        [
            InlineKeyboardButton("Growth", callback_data="growth"),
            InlineKeyboardButton("Elite", callback_data="elite"),
        ],
        [
            InlineKeyboardButton("Dream", callback_data="dream"),
            InlineKeyboardButton("CB 2", callback_data="cb2"),
        ],
        [
            InlineKeyboardButton("Early Excel", callback_data="earlyexcel"),
            InlineKeyboardButton("CC 3", callback_data="cc3"),
        ],
        [
            InlineKeyboardButton("CB 4", callback_data="cb4"),
            InlineKeyboardButton("CE 4", callback_data="ce4"),
        ],
        [
            InlineKeyboardButton("Conquer 1", callback_data="cq1"),
            InlineKeyboardButton("Conquer 2", callback_data="cq2"),
        ],
        [
            InlineKeyboardButton("✗", callback_data="close"),
            InlineKeyboardButton("⇒⇒", callback_data="sb_start_2"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_photo( photo = SB_IMAGE,
        caption = """ 🌀CHOOSE THE BATCH:


🌱 Page  1/2
        """,
        reply_markup=reply_markup
    )
