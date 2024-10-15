
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

ELP_PIC = "https://te.legra.ph/file/2efb32bb5ee28cb7f3534.jpg"


@Bot.on_message(filters.command('elp') & filters.private & subscribed , group=2005)
async def help(bot: Bot, message: Message):
        await message.reply_photo(photo = ELP_PIC,
            caption = """🌀CHOOSE THE BATCH:""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("Master Pro 1", callback_data="mp1_1"),
            InlineKeyboardButton("Master Pro 2", callback_data="mp2_1"),
        ],
        [
            InlineKeyboardButton("Growth", callback_data="growth_1"),
            InlineKeyboardButton("Elite", callback_data="elite_1"),
        ],
        [
            InlineKeyboardButton("Dream", callback_data="dream_1"),
            InlineKeyboardButton("CB 2", callback_data="cb2_1"),
        ],
        [
            InlineKeyboardButton("Early Excel", callback_data="earlyexcel_1"),
            InlineKeyboardButton("CC 3", callback_data="cc3_1"),
        ],
        [
            InlineKeyboardButton("CB 4", callback_data="cb4_1"),
            InlineKeyboardButton("CE 4", callback_data="ce4_1"),
        ],
        [
            InlineKeyboardButton("Conquer 1", callback_data="cq1_1"),
            InlineKeyboardButton("Conquer 2", callback_data="cq2_1"),
        ],
        [
            InlineKeyboardButton("Conquer 11", callback_data="cq11_1"),
            InlineKeyboardButton("Conquer 13", callback_data="cq13_1"),
        ],
        [
            InlineKeyboardButton("Conquer-3(Hindi)", callback_data="cq3_1"),
            InlineKeyboardButton("Conquer 9(Hindi)", callback_data="cq9_1"),
        ], 
        [
            InlineKeyboardButton("✗", callback_data="close"),
        ],            
        
        ]
    ),
    parse_mode=ParseMode.MARKDOWN,        
    )
@Bot.on_message(filters.command('elp') & filters.private,group=2005)
async def not_joined(client: Bot, message: Message):
    buttons = fsub_button(client, message)
    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=f"@{message.from_user.username}"
            if message.from_user.username
            else None,
            mention=message.from_user.mention,
            id=message.from_user.id,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True,
    )
