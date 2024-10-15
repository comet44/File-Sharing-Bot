
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=10093)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    list_info = [] 
    if data == "list_ioc":
      list_info = [
        f''' PCl₅✅ NCl₅ ❌SF₄✅ OF₄❌

SF₆✅ OF₆❌ SiF₆⁻²✅ CF₆⁻²❌

AIF₆⁻³✅ BF₆⁻³❌ PCl₆⁻✅ NCl₆⁻❌



SF₄✅ SH₄❌SF₆✅SH₆❌

PCl₅✅ PH₅❌  BrF₃✅ BrH₃❌

XeF₂✅ XeH₂❌ XeF₄✅ XeH₄❌

XeF₆✅ XeH₆❌


PF₆⁻ ✅PCl₆⁻❌PBr₆⁻❌ PI₆⁻❌

SiF₆⁻²✅SiCl₆⁻²❌SiBr₆⁻²❌SiI₆⁻²❌

IF₇✅ ICl₇❌ IBr₇❌

XeF₂✅ XeCl₂❌ XeF₄✅ XeCl₄❌

SiCl₆⁻²❌ TeCl₆⁻²✅

BrCl₅❌  ICl₅✅ ''',
                
        
              
        
    ]
    
    # Send each piece of information as a separate message
    for info in list_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
    
        parse_mode=ParseMode.MARKDOWN,
        
