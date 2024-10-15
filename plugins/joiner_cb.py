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
    if query.data.startswith('group_'):  # Ensure this is a group join request
        
        try:
            # Extract group ID from callback data
            group_id = int(query.data.split('_')[1])

            # Set expiration time for 15 seconds
            expiration_time = datetime.now() + timedelta(seconds=15)

            # Fetch group info (optional, based on your needs)
            chat = await client.get_chat(group_id)
            member = await client.get_chat_member(group_id, client.me.id)

            # Check if bot has the necessary permissions
            if not member.status in ['administrator', 'owner']:
                await query.message.reply_text("I need to be an admin in the group to generate invite links.")
                return

            # Generate the join link for the specified group with expiration and join request
            link = await client.create_chat_invite_link(
                group_id,
                expire_date=expiration_time,
                creates_join_request=True
            )

            # Send the link to the user using reply_text
            deca = await query.message.reply_text(
                f"<b>🍃 Here is the joining link (valid for 15 seconds)</b>: <a href='{link.invite_link}'>Click Here To Join</a>",
                disable_web_page_preview=True,
                protect_content=True,
            )

            # Wait for 15 seconds before revoking the link
            await asyncio.sleep(15)

            # Revoke the invite link after 15 seconds
            await client.revoke_chat_invite_link(group_id, link.invite_link)
            await deca.delete()

            # Inform the user that the link has expired
            await query.message.reply_text("The invite link has expired.")

        except Exception as e:
            # Handle any errors that may occur (like missing permissions, etc.)
            await query.message.reply_text(f"Sorry, I was unable to generate the join link. Please try again later. Error: {str(e)}")
