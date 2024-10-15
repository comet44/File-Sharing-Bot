#help call back 
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters

@Bot.on_callback_query(group=250)
async def hlpcallback(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help_cb":
        await query.message.edit_text(
            text = f'''Hey there... I'm unacademy lectures bot <a href=https://telegra.ph/file/00314693350157a35db7c.jpg> </a> \n .''',
            disable_web_page_preview = False,
            reply_markup = InlineKeyboardMarkup(
                [
                   [
                       InlineKeyboardButton("AKM SIR",   callback_data= "help_akm"),
                       InlineKeyboardButton("AG SIR ",   callback_data= "help_ath"),
                       InlineKeyboardButton("DR AG SIR ", callback_data= "help_dr"),
                   ],
                   [
                       InlineKeyboardButton("YSY SIR", callback_data= "help_ysy"),
                       InlineKeyboardButton("AB SIR", callback_data= "help_ab"),
                       InlineKeyboardButton("RS SIR", callback_data= "help_rs"),
                   ],
                   [
                        InlineKeyboardButton("ACID SIR ", callback_data= "help_acid"),
                        InlineKeyboardButton("IA SIR ", callback_data= "help_ia"), 
                        InlineKeyboardButton("RD SIR ", callback_data= "help_rd"),
                   ],
                   [
                        InlineKeyboardButton("ST SIR ", callback_data= "help_st"),
                        InlineKeyboardButton("JS SIR ", callback_data= "help_js"), 
                        InlineKeyboardButton("TNM SIR ", callback_data= "help_tnm"),
                   ],
                   [
                        InlineKeyboardButton("SKC SIR ", callback_data= "help_skc"),
                        InlineKeyboardButton("AKG SIR ", callback_data= "help_anu"), 
                        InlineKeyboardButton("PB SIR  ", callback_data= "help_pb"),
                   ],
                   [
                       
                       InlineKeyboardButton("Close", callback_data= "close"),
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
