#(©)Codexbotz


from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Bot.on_callback_query(group=28)
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "start_cb":
        await query.message.edit_text(
            text = f''' 
┏━━━━━━⊱✙⊰━━━━━━━━━━
┃✨Hey, I'm Raven
┃ ×Use The Buttons Below 
┃  To Know My Abilities ×
┗━━━━━━⊱✙⊰━━━━━━━━━━
''',
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
        InlineKeyboardButton(text="🤴 Owner ", url=f"https://t.me/rajharsh77"),
        
    ],            
    [
        InlineKeyboardButton(text="🌱Access Lectures", callback_data="ch_cb"),
    ],
    [
        InlineKeyboardButton(text="☘️ About", callback_data="about"),
        InlineKeyboardButton(text="📓 Info", callback_data="cmd")
    ],
   
                ]
            )
        )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
