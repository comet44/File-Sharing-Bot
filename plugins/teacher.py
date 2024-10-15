
import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot

from helper_func import subscribed, encode, decode, get_messages

SB_IMAGE = "https://te.legra.ph/file/e4f584bc01f67f2615c53.jpg"


@Bot.on_message(filters.command("unateachers") & filters.private & subscribed , group=8787)
async def stream_start(_: Client, message: Message):
    keyboard = [
        [
            InlineKeyboardButton("Master Pro 1", callback_data="teamp1"),
            InlineKeyboardButton("Master Pro 2", callback_data="teamp2"),
        ],
        [
            InlineKeyboardButton("Growth", callback_data="teagrowth"),
            InlineKeyboardButton("Elite", callback_data="teaelite"),
        ],
        [
            InlineKeyboardButton("Dream", callback_data="teadream"),
            InlineKeyboardButton("CB 2", callback_data="teacb2"),
        ],
        [
            InlineKeyboardButton("Early Excel", callback_data="teaearlyexcel"),
            InlineKeyboardButton("CC 3", callback_data="teacc3"),
        ],
        [
            InlineKeyboardButton("CB 4", callback_data="teacb4"),
            InlineKeyboardButton("CE 4", callback_data="teace4"),
        ],
        [
            InlineKeyboardButton("Conquer 1", callback_data="teacq1"),
            InlineKeyboardButton("Conquer 2", callback_data="teacq2"),
        ],
        [
            InlineKeyboardButton("Conquer 4", callback_data="teacq4"),
            InlineKeyboardButton("Conquer 8", callback_data="teacq8"),
        ],
        [
            InlineKeyboardButton("Conquer 11", callback_data="teacq11"),
            InlineKeyboardButton("Conquer 13", callback_data="teacq13"),
        ],
        [
            InlineKeyboardButton("✗", callback_data="close"),
          
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_photo( photo = SB_IMAGE,
        caption = """CHOOSE THE BATCH:


🌱 Page  1/1
        """,
        reply_markup=reply_markup
    )
