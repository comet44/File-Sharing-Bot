from bot import Bot
from pyrogram.types import Message
import asyncio
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT
from datetime import datetime
from helper_func import get_readable_time

ERROR_TEXT = "Invalid Command press /start "

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming & ~filters.command(['lectures','solution','help','notes','info','joiner_start','chat','test','stream','elp','unateachers','unabatches','join']))
async def useless(_,message: Message):
    if ERROR_TEXT:
        await message.reply(ERROR_TEXT)
