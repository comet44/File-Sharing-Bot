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
    if not query.data.startswith('group_'):
        return  # Ignore non-group callback queries
    
    group_id = int(query.data.split('_')[1])    # Convert group_id back to int
    try:
        expiration_time = datetime.now() + timedelta(minutes=15)

          # Wait 5 seconds before fetching group info
        chat = await client.get_chat(group_id) 
        member = await client.get_chat_member(group_id, client.me.id)# Refresh group info after delay


        # Generate the join link for the specified group
        link = await client.create_chat_invite_link(
            group_id,
            expire_date=expiration_time,
            creates_join_request=True
        )

        # Send the link to the user using reply_text
        deca= await query.message.reply_text(f"<b>🍃 Here is Joining link (valid for only 15 Seconds)</b>: <a href='{link.invite_link}'>Click Here To Join</a>)" , disable_web_page_preview = True , protect_content=True, )

        # Wait for 3 minutes before revoking the link
        await asyncio.sleep(15)  # 3 minutes (you mentioned 3 minutes in the message, not 15)
        await client.revoke_chat_invite_link(group_id, link.invite_link)
        await deca.delete()
        
        # Inform the user that the link has expired
        await query.message.reply_text("The Invite  link has expired.")

    except Exception as e:
        # Send the error message using reply_text
        await query.message.reply_text(f"Sorry, I was unable to generate the join link. Please Try Again Later")
