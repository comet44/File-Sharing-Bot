#(©)Codexbotz


from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Bot.on_callback_query(group=871)
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "cmd":
        await query.message.edit_text(
            text = f'''
🪐Commands 

/lectures - Get Video Lectures 

/test - Get Test PDF


''',
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data = "start_cb")
                    ]
                ]
            )
        )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
