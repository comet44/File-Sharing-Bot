import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from datetime import datetime, timedelta
from aiohttp import ClientSession
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message



GROUPS = {
    "Group 1": -1001506454180,  # Replace with your actual group IDs
    "Group 2": -1001814803421,  # Replace with your actual group IDs
    "Group 3": -1009876543210   # Replace with your actual group IDs
}


@Bot.on_message(filters.command('join') & filters.private, group=89897)
async def join_command(bot, message):
    # Create inline buttons for each group, ensuring callback_data is a string
    buttons = [
        [InlineKeyboardButton(group_name, callback_data=str(group_id))] for group_name, group_id in GROUPS.items()
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        message.chat.id,
        "Choose a group to join:",
        reply_markup=reply_markup
    )

