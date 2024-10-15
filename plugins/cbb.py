#(©)Codexbotz


from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user
from pyrogram.enums import ParseMode

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        
        user_first_name = query.from_user.first_name
        users = await full_userbase()
        await query.message.edit_text(
            text = f'''
🪐**Hey there! `{user_first_name}`**

🌀**Current Users** : {len(users)} Users 

☘️I'm here to make your Learning fun and easy! 

Any issues or need help related to me? Come visit us in Support Chat @Rajharsh777

This Bot Is  Licensed Under The GNU (General Public License v3.0)

''',
            disable_web_page_preview = True,
            parse_mode = ParseMode.MARKDOWN,
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
