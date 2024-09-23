import json
import time
import asyncio


from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from datetime import datetime, timedelta
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID


@Bot.on_callback_query(group=77687)
async def handle_callback_query(client: Bot, query: CallbackQuery):
    group_id = int(query.data)  # Convert group_id back to int
    try:
        expiration_time = datetime.now() + timedelta(minutes=15)

        # Generate the join link for the specified group
        link = await Bot.create_chat_invite_link(
            group_id,
            expire_date=expiration_time,
            creates_join_request=True
        )

        # Send the link to the user
        await Bot.send_message(query.message.chat.id, f"Join link (valid for 3 minutes): {link.invite_link}")

        # Wait for 15 minutes before revoking the link
        await asyncio.sleep(180)  # 15 minutes
        await Bot.revoke_chat_invite_link(group_id, link.invite_link)
        await Bot.send_message(query.message.chat.id, "The join link has expired.")

    except Exception as e:
        await Bot.send_message(query.message.chat.id, f"Sorry, I was unable to generate the join link. Error: {str(e)}")
