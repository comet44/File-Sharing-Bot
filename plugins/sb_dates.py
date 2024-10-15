import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM,PROTECT_CONTENT



@Bot.on_callback_query(group=345)
async def hlpcallback(client: Bot, query: CallbackQuery):
    data = query.data
    button_number = 1
    if data == "junmp1":
     await query.message.edit_text(
        """🌀 BATCH NAME »» Master Pro 1

🌱 Full Name »» Abhinav Batch for NEET 2024
🌀 Start At: 14 June, 2023

✅ MONTH »» Jun 2023
""",
        reply_markup=InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton("1", callback_data=f"junmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"junmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"junmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"junmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"junmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"junmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"junmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"junmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"junmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"junmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"junmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"junmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"junmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"junmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"junmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"junmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"junmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"junmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"junmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"junmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"junmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"junmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"junmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"junmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"junmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"junmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"junmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"junmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"junmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"junmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"junmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
        )
    )
    elif data == "julmp1":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 1

🌱 Full Name »» Abhinav Batch for NEET 2024
🌀 Start At: 14 June, 2023

✅ MONTH »» Jul 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"mp_1"),
        ],
        ]
    )
    )
    elif data == "augmp1":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 1

🌱 Full Name »» Abhinav Batch for NEET 2024
🌀 Start At: 14 June, 2023

✅ MONTH »» Aug 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septmp1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 1

🌱 Full Name »» Abhinav Batch for NEET 2024
🌀 Start At: 14 June, 2023

✅ MONTH »» Sept 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octmp1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 1

🌱 Full Name »» Abhinav Batch for NEET 2024
🌀 Start At: 14 June, 2023

✅ MONTH »» Oct 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novmp1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 1

🌱 Full Name »» Abhinav Batch for NEET 2024
🌀 Start At: 14 June, 2023

✅ MONTH »» Nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "decmp1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »»  Master Pro 1

🌱 Full Name »» `Abhinav Batch for NEET 2024`
🌀 Start At:  14 June, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"decmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"decmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"decmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"decmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"decmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"decmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"decmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"decmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"decmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"decmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"decmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"decmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"decmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"decmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"decmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"decmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"decmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"decmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"decmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"decmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"decmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"decmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"decmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"decmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"decmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"decmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"decmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"decmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"decmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"decmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"decmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "janmp1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »»  Master Pro 1

🌱 Full Name »» `Abhinav Batch for NEET 2024`
🌀 Start At:  14 June, 2023

✅ MONTH »» jan 2024
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"janmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"janmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"janmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"janmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"janmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"janmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"janmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"janmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"janmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"janmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"janmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"janmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"janmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"janmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"janmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"janmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"janmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"janmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"janmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"janmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"janmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"janmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"janmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"janmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"janmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"janmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"janmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"janmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"janmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"janmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"janmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    ) 
    elif data == "febmp1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »»  Master Pro 1

🌱 Full Name »» `Abhinav Batch for NEET 2024`
🌀 Start At:  14 June, 2023

✅ MONTH »» feb 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"febmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"febmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"febmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"febmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"febmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"febmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"febmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"febmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"febmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"febmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"febmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"febmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"febmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"febmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"febmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"febmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"febmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"febmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"febmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"febmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"febmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"febmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"febmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"febmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"febmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"febmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"febmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"febmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"febmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"febmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"febmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    ) 
    elif data == "marmp1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »»  Master Pro 1

🌱 Full Name »» `Abhinav Batch for NEET 2024`
🌀 Start At:  14 June, 2023

✅ MONTH »» mar 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"marmp1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"marmp1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"marmp1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"marmp1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"marmp1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"marmp1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"marmp1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"marmp1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"marmp1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"marmp1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"marmp1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"marmp1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"marmp1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"marmp1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"marmp1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"marmp1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"marmp1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"marmp1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"marmp1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"marmp1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"marmp1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"marmp1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"marmp1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"marmp1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"marmp1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"marmp1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"marmp1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"marmp1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"marmp1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"marmp1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"marmp1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )            
    elif data == "julmp2":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 2

🌱 Full Name »» Prashiksha Batch NEET UG 2024
🌀 Start At: 3 July, 2023

✅ MONTH »» Jul 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julmp2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julmp2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julmp2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julmp2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julmp2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julmp2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julmp2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julmp2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julmp2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julmp2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julmp2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julmp2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julmp2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julmp2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julmp2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julmp2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julmp2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julmp2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julmp2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julmp2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julmp2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julmp2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julmp2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julmp2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julmp2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julmp2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julmp2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julmp2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julmp2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julmp2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julmp2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"mp_1"),
        ],
        ]
    )
    )
    elif data == "augmp2":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 2

🌱 Full Name »» Prashiksha Batch NEET UG 2024
🌀 Start At: 3 July, 2023

✅ MONTH »» Aug 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augmp2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augmp2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augmp2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augmp2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augmp2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augmp2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augmp2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augmp2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augmp2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augmp2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augmp2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augmp2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augmp2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augmp2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augmp2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augmp2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augmp2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augmp2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augmp2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augmp2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augmp2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augmp2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augmp2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augmp2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augmp2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augmp2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augmp2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augmp2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augmp2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augmp2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augmp2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septmp2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 2

🌱 Full Name »» Prashiksha Batch NEET UG 2024
🌀 Start At: 3 July, 2023

✅ MONTH »» Sept 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septmp2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septmp2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septmp2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septmp2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septmp2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septmp2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septmp2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septmp2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septmp2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septmp2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septmp2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septmp2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septmp2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septmp2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septmp2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septmp2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septmp2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septmp2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septmp2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septmp2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septmp2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septmp2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septmp2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septmp2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septmp2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septmp2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septmp2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septmp2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septmp2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septmp2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septmp2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octmp2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 2

🌱 Full Name »» Prashiksha Batch NEET UG 2024
🌀 Start At: 3 July, 2023

✅ MONTH »» Oct 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octmp2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octmp2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octmp2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octmp2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octmp2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octmp2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octmp2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octmp2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octmp2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octmp2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octmp2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octmp2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octmp2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octmp2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octmp2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octmp2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octmp2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octmp2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octmp2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octmp2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octmp2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octmp2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octmp2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octmp2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octmp2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octmp2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octmp2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octmp2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octmp2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octmp2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octmp2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novmp2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Master Pro 2

🌱 Full Name »» Prashiksha Batch NEET UG 2024
🌀 Start At: 3 July, 2023

✅ MONTH »» Nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novmp2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novmp2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novmp2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novmp2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novmp2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novmp2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novmp2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novmp2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novmp2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novmp2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novmp2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novmp2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novmp2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novmp2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novmp2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novmp2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novmp2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novmp2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novmp2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novmp2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novmp2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novmp2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novmp2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novmp2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novmp2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novmp2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novmp2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novmp2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novmp2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novmp2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novmp2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp_1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "decmp2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »»  Master Pro 2

🌱 Full Name »» `Prashiksha Batch NEET UG 2024`
🌀 Start At:  3 July, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"decmp2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"decmp2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"decmp2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"decmp2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"decmp2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"decmp2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"decmp2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"decmp2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"decmp2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"decmp2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"decmp2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"decmp2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"decmp2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"decmp2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"decmp2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"decmp2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"decmp2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"decmp2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"decmp2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"decmp2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"decmp2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"decmp2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"decmp2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"decmp2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"decmp2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"decmp2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"decmp2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"decmp2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"decmp2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"decmp2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"decmp2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"mp2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "jundream":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Dream Batch

🌱 Full Name »» `Dream Batch for NEET UG 2024`
🌀 Start At:  7 June, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"jundream_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"jundream_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"jundream_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"jundream_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"jundream_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"jundream_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"jundream_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"jundream_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"jundream_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"jundream_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"jundream_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"jundream_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"jundream_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"jundream_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"jundream_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"jundream_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"jundream_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"jundream_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"jundream_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"jundream_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"jundream_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"jundream_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"jundream_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"jundream_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"jundream_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"jundream_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"jundream_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"jundream_{button_number + 27}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"back"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],            
        ]
    )
    )        
    elif data == "juldream":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Dream Batch

🌱 Full Name »» `Dream Batch for NEET UG 2024`
🌀 Start At:  7 June, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"juldream_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"juldream_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"juldream_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"juldream_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"juldream_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"juldream_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"juldream_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"juldream_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"juldream_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"juldream_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"juldream_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"juldream_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"juldream_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"juldream_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"juldream_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"juldream_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"juldream_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"juldream_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"juldream_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"juldream_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"juldream_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"juldream_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"juldream_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"juldream_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"juldream_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"juldream_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"juldream_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"juldream_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"juldream_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"juldream_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"juldream_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"dream"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augdream":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Dream Batch

🌱 Full Name »» `Dream Batch for NEET UG 2024`
🌀 Start At:  7 June, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augdream_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augdream_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augdream_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augdream_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augdream_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augdream_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augdream_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augdream_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augdream_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augdream_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augdream_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augdream_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augdream_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augdream_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augdream_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augdream_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augdream_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augdream_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augdream_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augdream_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augdream_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augdream_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augdream_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augdream_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augdream_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augdream_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augdream_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augdream_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augdream_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augdream_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augdream_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"dream"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septdream":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Dream Batch

🌱 Full Name »» `Dream Batch for NEET UG 2024`
🌀 Start At:  7 June, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septdream_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septdream_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septdream_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septdream_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septdream_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septdream_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septdream_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septdream_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septdream_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septdream_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septdream_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septdream_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septdream_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septdream_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septdream_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septdream_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septdream_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septdream_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septdream_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septdream_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septdream_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septdream_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septdream_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septdream_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septdream_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septdream_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septdream_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septdream_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septdream_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septdream_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septdream_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"dream"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octdream":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Dream Batch

🌱 Full Name »» `Dream Batch for NEET UG 2024`
🌀 Start At:  7 June, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octdream_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octdream_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octdream_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octdream_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octdream_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octdream_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octdream_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octdream_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octdream_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octdream_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octdream_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octdream_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octdream_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octdream_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octdream_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octdream_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octdream_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octdream_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octdream_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octdream_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octdream_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octdream_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octdream_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octdream_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octdream_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octdream_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octdream_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octdream_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octdream_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octdream_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octdream_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"dream"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novdream":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Dream Batch

🌱 Full Name »» `Dream Batch for NEET UG 2024`
🌀 Start At:  7 June, 2023

✅ MONTH »» Nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novdream_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novdream_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novdream_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novdream_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novdream_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novdream_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novdream_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novdream_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novdream_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novdream_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novdream_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novdream_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novdream_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novdream_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novdream_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novdream_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novdream_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novdream_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novdream_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novdream_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novdream_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novdream_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novdream_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novdream_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novdream_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novdream_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novdream_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novdream_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novdream_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novdream_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novdream_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"dream"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "decdream":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Dream Batch

🌱 Full Name »» `Dream Batch for NEET UG 2024`
🌀 Start At:  7 June, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"decdream_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"decdream_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"decdream_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"decdream_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"decdream_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"decdream_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"decdream_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"decdream_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"decdream_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"decdream_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"decdream_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"decdream_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"decdream_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"decdream_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"decdream_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"decdream_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"decdream_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"decdream_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"decdream_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"decdream_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"decdream_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"decdream_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"decdream_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"decdream_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"decdream_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"decdream_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"decdream_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"decdream_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"decdream_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"decdream_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"decdream_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"dream"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "janearlyexcel":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» jan 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"janearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"janearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"janearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"janearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"janearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"janearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"janearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"janearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"janearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"janearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"janearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"janearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"janearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"janearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"janearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"janearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"janearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"janearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"janearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"janearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"janearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"janearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"janearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"janearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"janearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"janearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"janearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"janearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"janearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"janearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"janearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
        )
    elif data == "febearlyexcel":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 20237 e, 2023

✅ MONTH »» Feb 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"febearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"febearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"febearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"febearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"febearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"febearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"febearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"febearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"febearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"febearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"febearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"febearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"febearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"febearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"febearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"febearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"febearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"febearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"febearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"febearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"febearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"febearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"febearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"febearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"febearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"febearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"febearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"febearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"febearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"febearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"febearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
        )
    elif data == "marearlyexcel":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» Mar 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"marearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"marearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"marearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"marearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"marearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"marearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"marearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"marearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"marearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"marearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"marearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"marearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"marearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"marearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"marearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"marearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"marearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"marearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"marearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"marearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"marearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"marearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"marearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"marearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"marearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"marearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"marearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"marearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"marearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"marearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"marearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "aprearlyexcel":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» Apr 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"aprearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"aprearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"aprearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"aprearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"aprearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"aprearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"aprearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"aprearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"aprearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"aprearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"aprearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"aprearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"aprearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"aprearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"aprearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"aprearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"aprearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"aprearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"aprearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"aprearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"aprearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"aprearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"aprearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"aprearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"aprearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"aprearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"aprearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"aprearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"aprearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"aprearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"aprearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )
    elif data == "mayearlyexcel":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» May 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"mayearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"mayearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"mayearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"mayearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"mayearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"mayearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"mayearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"mayearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"mayearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"mayearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"mayearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"mayearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"mayearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"mayearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"mayearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"mayearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"mayearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"mayearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"mayearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"mayearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"mayearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"mayearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"mayearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"mayearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"mayearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"mayearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"mayearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"mayearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"mayearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"mayearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"mayearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )
    elif data == "junearlyexcel":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» Jun 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"junearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"junearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"junearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"junearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"junearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"junearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"junearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"junearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"junearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"junearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"junearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"junearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"junearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"junearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"junearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"junearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"junearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"junearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"junearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"junearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"junearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"junearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"junearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"junearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"junearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"junearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"junearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"junearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"junearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"junearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"junearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "julearlyexcel":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augearlyexcel":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septearlyexcel":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octearlyexcel":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novearlyexcel":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "decearlyexcel":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Early Excel 1

🌱 Full Name »» `Kota Early Excel 1 for NEET UG 2024`
🌀 Start At:  27 January, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"decearlyexcel_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"decearlyexcel_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"decearlyexcel_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"decearlyexcel_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"decearlyexcel_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"decearlyexcel_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"decearlyexcel_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"decearlyexcel_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"decearlyexcel_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"decearlyexcel_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"decearlyexcel_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"decearlyexcel_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"decearlyexcel_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"decearlyexcel_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"decearlyexcel_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"decearlyexcel_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"decearlyexcel_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"decearlyexcel_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"decearlyexcel_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"decearlyexcel_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"decearlyexcel_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"decearlyexcel_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"decearlyexcel_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"decearlyexcel_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"decearlyexcel_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"decearlyexcel_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"decearlyexcel_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"decearlyexcel_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"decearlyexcel_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"decearlyexcel_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"decearlyexcel_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"earlyexcel"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "maycb2":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-2

🌱 Full Name »» `Kota NEET UG 2024 CB-2`
🌀 Start At:  15 May, 2023

✅ MONTH »» May 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"maycb2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"maycb2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"maycb2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"maycb2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"maycb2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"maycb2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"maycb2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"maycb2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"maycb2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"maycb2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"maycb2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"maycb2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"maycb2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"maycb2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"maycb2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"maycb2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"maycb2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"maycb2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"maycb2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"maycb2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"maycb2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"maycb2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"maycb2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"maycb2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"maycb2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"maycb2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"maycb2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"maycb2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"maycb2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"maycb2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"maycb2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )
    elif data == "juncb2":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-2

🌱 Full Name »» `Kota NEET UG 2024 CB-2`
🌀 Start At:  15 May, 2023

✅ MONTH »» Jun 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"juncb2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"juncb2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"juncb2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"juncb2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"juncb2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"juncb2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"juncb2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"juncb2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"juncb2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"juncb2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"juncb2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"juncb2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"juncb2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"juncb2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"juncb2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"juncb2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"juncb2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"juncb2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"juncb2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"juncb2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"juncb2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"juncb2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"juncb2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"juncb2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"juncb2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"juncb2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"juncb2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"juncb2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"juncb2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"juncb2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"juncb2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "julcb2":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-2

🌱 Full Name »» `Kota NEET UG 2024 CB-2`
🌀 Start At:  15 May, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julcb2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julcb2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julcb2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julcb2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julcb2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julcb2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julcb2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julcb2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julcb2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julcb2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julcb2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julcb2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julcb2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julcb2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julcb2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julcb2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julcb2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julcb2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julcb2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julcb2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julcb2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julcb2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julcb2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julcb2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julcb2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julcb2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julcb2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julcb2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julcb2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julcb2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julcb2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augcb2":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-2

🌱 Full Name »» `Kota NEET UG 2024 CB-2`
🌀 Start At:  15 May, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augcb2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augcb2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augcb2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augcb2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augcb2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augcb2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augcb2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augcb2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augcb2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augcb2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augcb2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augcb2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augcb2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augcb2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augcb2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augcb2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augcb2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augcb2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augcb2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augcb2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augcb2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augcb2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augcb2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augcb2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augcb2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augcb2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augcb2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augcb2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augcb2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augcb2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augcb2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septcb2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-2

🌱 Full Name »» `Kota NEET UG 2024 CB-2`
🌀 Start At:  15 May, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septcb2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septcb2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septcb2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septcb2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septcb2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septcb2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septcb2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septcb2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septcb2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septcb2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septcb2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septcb2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septcb2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septcb2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septcb2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septcb2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septcb2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septcb2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septcb2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septcb2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septcb2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septcb2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septcb2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septcb2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septcb2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septcb2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septcb2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septcb2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septcb2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septcb2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septcb2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octcb2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-2

🌱 Full Name »» `Kota NEET UG 2024 CB-2`
🌀 Start At:  15 May, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octcb2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octcb2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octcb2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octcb2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octcb2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octcb2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octcb2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octcb2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octcb2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octcb2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octcb2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octcb2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octcb2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octcb2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octcb2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octcb2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octcb2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octcb2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octcb2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octcb2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octcb2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octcb2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octcb2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octcb2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octcb2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octcb2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octcb2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octcb2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octcb2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octcb2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octcb2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novcb2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-2

🌱 Full Name »» `Kota NEET UG 2024 CB-2`
🌀 Start At:  15 May, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novcb2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novcb2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novcb2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novcb2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novcb2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novcb2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novcb2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novcb2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novcb2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novcb2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novcb2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novcb2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novcb2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novcb2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novcb2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novcb2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novcb2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novcb2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novcb2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novcb2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novcb2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novcb2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novcb2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novcb2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novcb2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novcb2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novcb2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novcb2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novcb2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novcb2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novcb2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "deccb2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-2

🌱 Full Name »» `Kota NEET UG 2024 CB-2`
🌀 Start At:  15 May, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"deccb2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"deccb2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"deccb2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"deccb2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"deccb2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"deccb2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"deccb2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"deccb2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"deccb2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"deccb2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"deccb2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"deccb2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"deccb2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"deccb2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"deccb2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"deccb2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"deccb2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"deccb2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"deccb2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"deccb2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"deccb2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"deccb2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"deccb2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"deccb2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"deccb2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"deccb2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"deccb2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"deccb2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"deccb2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"deccb2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"deccb2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "jungrowth":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Growth Batch

🌱 Full Name »» `Akshar Batch for NEET 2025`
🌀 Start At:  9 June, 2023

✅ MONTH »» Jun 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"jungrowth_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"jungrowth_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"jungrowth_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"jungrowth_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"jungrowth_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"jungrowth_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"jungrowth_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"jungrowth_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"jungrowth_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"jungrowth_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"jungrowth_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"jungrowth_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"jungrowth_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"jungrowth_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"jungrowth_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"jungrowth_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"jungrowth_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"jungrowth_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"jungrowth_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"jungrowth_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"jungrowth_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"jungrowth_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"jungrowth_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"jungrowth_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"jungrowth_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"jungrowth_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"jungrowth_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"jungrowth_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"jungrowth_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"jungrowth_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"jungrowth_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"growth"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "julgrowth":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Growth Batch

🌱 Full Name »» `Akshar Batch for NEET 2025`
🌀 Start At:  9 June, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julgrowth_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julgrowth_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julgrowth_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julgrowth_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julgrowth_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julgrowth_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julgrowth_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julgrowth_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julgrowth_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julgrowth_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julgrowth_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julgrowth_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julgrowth_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julgrowth_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julgrowth_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julgrowth_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julgrowth_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julgrowth_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julgrowth_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julgrowth_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julgrowth_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julgrowth_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julgrowth_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julgrowth_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julgrowth_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julgrowth_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julgrowth_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julgrowth_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julgrowth_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julgrowth_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julgrowth_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"growth"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "auggrowth":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Growth Batch

🌱 Full Name »» `Akshar Batch for NEET 2025`
🌀 Start At:  9 June, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"auggrowth_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"auggrowth_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"auggrowth_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"auggrowth_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"auggrowth_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"auggrowth_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"auggrowth_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"auggrowth_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"auggrowth_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"auggrowth_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"auggrowth_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"auggrowth_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"auggrowth_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"auggrowth_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"auggrowth_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"auggrowth_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"auggrowth_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"auggrowth_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"auggrowth_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"auggrowth_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"auggrowth_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"auggrowth_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"auggrowth_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"auggrowth_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"auggrowth_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"auggrowth_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"auggrowth_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"auggrowth_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"auggrowth_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"auggrowth_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"auggrowth_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"growth"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septgrowth":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Growth Batch

🌱 Full Name »» `Akshar Batch for NEET 2025`
🌀 Start At:  9 June, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septgrowth_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septgrowth_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septgrowth_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septgrowth_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septgrowth_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septgrowth_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septgrowth_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septgrowth_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septgrowth_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septgrowth_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septgrowth_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septgrowth_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septgrowth_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septgrowth_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septgrowth_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septgrowth_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septgrowth_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septgrowth_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septgrowth_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septgrowth_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septgrowth_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septgrowth_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septgrowth_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septgrowth_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septgrowth_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septgrowth_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septgrowth_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septgrowth_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septgrowth_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septgrowth_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septgrowth_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"growth"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octgrowth":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Growth Batch

🌱 Full Name »» `Akshar Batch for NEET 2025`
🌀 Start At:  9 June, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octgrowth_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octgrowth_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octgrowth_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octgrowth_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octgrowth_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octgrowth_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octgrowth_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octgrowth_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octgrowth_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octgrowth_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octgrowth_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octgrowth_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octgrowth_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octgrowth_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octgrowth_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octgrowth_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octgrowth_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octgrowth_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octgrowth_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octgrowth_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octgrowth_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octgrowth_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octgrowth_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octgrowth_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octgrowth_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octgrowth_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octgrowth_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octgrowth_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octgrowth_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octgrowth_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octgrowth_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"growth"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novgrowth":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Growth Batch

🌱 Full Name »» `Akshar Batch for NEET 2025`
🌀 Start At:  9 June, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novgrowth_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novgrowth_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novgrowth_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novgrowth_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novgrowth_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novgrowth_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novgrowth_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novgrowth_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novgrowth_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novgrowth_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novgrowth_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novgrowth_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novgrowth_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novgrowth_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novgrowth_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novgrowth_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novgrowth_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novgrowth_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novgrowth_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novgrowth_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novgrowth_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novgrowth_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novgrowth_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novgrowth_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novgrowth_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novgrowth_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novgrowth_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novgrowth_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novgrowth_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novgrowth_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novgrowth_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"growth"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "decgrowth":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Growth Batch

🌱 Full Name »» `Akshar Batch for NEET 2025`
🌀 Start At:  9 June, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"decgrowth_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"decgrowth_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"decgrowth_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"decgrowth_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"decgrowth_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"decgrowth_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"decgrowth_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"decgrowth_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"decgrowth_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"decgrowth_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"decgrowth_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"decgrowth_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"decgrowth_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"decgrowth_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"decgrowth_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"decgrowth_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"decgrowth_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"decgrowth_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"decgrowth_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"decgrowth_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"decgrowth_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"decgrowth_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"decgrowth_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"decgrowth_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"decgrowth_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"decgrowth_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"decgrowth_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"decgrowth_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"decgrowth_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"decgrowth_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"decgrowth_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"growth"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "julelite":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Elite Batch

🌱 Full Name »» `Umang Batch NEET UG 2024 (Physics & Chemistry)`
🌀 Start At:  15 July, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julelite_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julelite_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julelite_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julelite_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julelite_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julelite_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julelite_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julelite_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julelite_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julelite_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julelite_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julelite_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julelite_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julelite_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julelite_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julelite_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julelite_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julelite_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julelite_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julelite_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julelite_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julelite_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julelite_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julelite_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julelite_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julelite_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julelite_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julelite_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julelite_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julelite_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julelite_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"elite"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augelite":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Elite Batch

🌱 Full Name »» `Umang Batch NEET UG 2024 (Physics & Chemistry)`
🌀 Start At:  15 July, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augelite_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augelite_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augelite_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augelite_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augelite_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augelite_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augelite_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augelite_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augelite_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augelite_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augelite_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augelite_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augelite_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augelite_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augelite_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augelite_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augelite_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augelite_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augelite_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augelite_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augelite_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augelite_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augelite_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augelite_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augelite_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augelite_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augelite_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augelite_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augelite_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augelite_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augelite_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"elite"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septelite":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Elite Batch

🌱 Full Name »» `Umang Batch NEET UG 2024 (Physics & Chemistry)`
🌀 Start At:  15 July, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septelite_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septelite_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septelite_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septelite_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septelite_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septelite_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septelite_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septelite_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septelite_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septelite_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septelite_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septelite_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septelite_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septelite_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septelite_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septelite_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septelite_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septelite_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septelite_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septelite_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septelite_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septelite_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septelite_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septelite_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septelite_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septelite_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septelite_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septelite_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septelite_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septelite_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septelite_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"elite"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octelite":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Elite Batch

🌱 Full Name »» `Umang Batch NEET UG 2024 (Physics & Chemistry)`
🌀 Start At:  15 July, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octelite_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octelite_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octelite_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octelite_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octelite_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octelite_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octelite_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octelite_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octelite_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octelite_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octelite_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octelite_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octelite_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octelite_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octelite_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octelite_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octelite_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octelite_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octelite_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octelite_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octelite_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octelite_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octelite_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octelite_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octelite_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octelite_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octelite_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octelite_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octelite_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octelite_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octelite_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"elite"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novelite":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Elite Batch

🌱 Full Name »» `Umang Batch NEET UG 2024 (Physics & Chemistry)`
🌀 Start At:  15 July, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novelite_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novelite_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novelite_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novelite_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novelite_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novelite_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novelite_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novelite_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novelite_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novelite_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novelite_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novelite_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novelite_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novelite_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novelite_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novelite_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novelite_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novelite_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novelite_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novelite_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novelite_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novelite_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novelite_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novelite_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novelite_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novelite_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novelite_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novelite_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novelite_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novelite_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novelite_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"elite"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "decelite":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Elite Batch

🌱 Full Name »» `Umang Batch NEET UG 2024 (Physics & Chemistry)`
🌀 Start At:  15 July, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"decelite_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"decelite_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"decelite_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"decelite_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"decelite_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"decelite_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"decelite_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"decelite_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"decelite_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"decelite_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"decelite_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"decelite_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"decelite_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"decelite_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"decelite_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"decelite_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"decelite_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"decelite_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"decelite_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"decelite_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"decelite_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"decelite_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"decelite_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"decelite_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"decelite_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"decelite_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"decelite_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"decelite_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"decelite_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"decelite_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"decelite_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"elite"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "maycc3":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CC-3

🌱 Full Name »» `Kota NEET UG 2024 CC-3`
🌀 Start At:  30 May, 2023

✅ MONTH »» May 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [    
            InlineKeyboardButton("30", callback_data=f"maycc3_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"maycc3_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cc3"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )
    elif data == "juncc3":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CC-3

🌱 Full Name »» `Kota NEET UG 2024 CC-3`
🌀 Start At:  30 May, 2023

✅ MONTH »» Jun 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"juncc3_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"juncc3_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"juncc3_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"juncc3_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"juncc3_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"juncc3_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"juncc3_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"juncc3_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"juncc3_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"juncc3_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"juncc3_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"juncc3_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"juncc3_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"juncc3_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"juncc3_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"juncc3_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"juncc3_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"juncc3_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"juncc3_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"juncc3_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"juncc3_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"juncc3_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"juncc3_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"juncc3_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"juncc3_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"juncc3_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"juncc3_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"juncc3_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"juncc3_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"juncc3_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"juncc3_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cc3"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "julcc3":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CC-3

🌱 Full Name »» `Kota NEET UG 2024 CC-3`
🌀 Start At:  30 May, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julcc3_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julcc3_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julcc3_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julcc3_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julcc3_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julcc3_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julcc3_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julcc3_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julcc3_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julcc3_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julcc3_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julcc3_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julcc3_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julcc3_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julcc3_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julcc3_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julcc3_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julcc3_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julcc3_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julcc3_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julcc3_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julcc3_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julcc3_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julcc3_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julcc3_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julcc3_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julcc3_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julcc3_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julcc3_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julcc3_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julcc3_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cc3"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augcc3":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CC-3

🌱 Full Name »» `Kota NEET UG 2024 CC-3`
🌀 Start At:  30 May, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augcc3_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augcc3_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augcc3_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augcc3_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augcc3_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augcc3_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augcc3_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augcc3_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augcc3_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augcc3_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augcc3_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augcc3_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augcc3_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augcc3_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augcc3_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augcc3_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augcc3_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augcc3_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augcc3_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augcc3_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augcc3_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augcc3_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augcc3_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augcc3_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augcc3_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augcc3_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augcc3_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augcc3_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augcc3_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augcc3_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augcc3_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cc3"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septcc3":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CC-3

🌱 Full Name »» `Kota NEET UG 2024 CC-3`
🌀 Start At:  30 May, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septcc3_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septcc3_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septcc3_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septcc3_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septcc3_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septcc3_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septcc3_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septcc3_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septcc3_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septcc3_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septcc3_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septcc3_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septcc3_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septcc3_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septcc3_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septcc3_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septcc3_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septcc3_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septcc3_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septcc3_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septcc3_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septcc3_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septcc3_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septcc3_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septcc3_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septcc3_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septcc3_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septcc3_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septcc3_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septcc3_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septcc3_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cc3"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octcc3":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CC-3

🌱 Full Name »» `Kota NEET UG 2024 CC-3`
🌀 Start At:  30 May, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octcc3_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octcc3_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octcc3_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octcc3_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octcc3_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octcc3_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octcc3_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octcc3_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octcc3_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octcc3_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octcc3_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octcc3_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octcc3_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octcc3_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octcc3_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octcc3_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octcc3_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octcc3_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octcc3_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octcc3_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octcc3_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octcc3_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octcc3_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octcc3_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octcc3_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octcc3_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octcc3_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octcc3_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octcc3_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octcc3_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octcc3_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cc3"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novcc3":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CC-3

🌱 Full Name »» `Kota NEET UG 2024 CC-3`
🌀 Start At:  30 May, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novcc3_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novcc3_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novcc3_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novcc3_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novcc3_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novcc3_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novcc3_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novcc3_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novcc3_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novcc3_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novcc3_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novcc3_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novcc3_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novcc3_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novcc3_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novcc3_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novcc3_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novcc3_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novcc3_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novcc3_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novcc3_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novcc3_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novcc3_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novcc3_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novcc3_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novcc3_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novcc3_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novcc3_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novcc3_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novcc3_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novcc3_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cc3"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "deccc3":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CC-3

🌱 Full Name »» `Kota NEET UG 2024 CC-3`
🌀 Start At:  30 May, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"deccc3_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"deccc3_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"deccc3_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"deccc3_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"deccc3_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"deccc3_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"deccc3_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"deccc3_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"deccc3_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"deccc3_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"deccc3_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"deccc3_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"deccc3_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"deccc3_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"deccc3_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"deccc3_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"deccc3_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"deccc3_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"deccc3_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"deccc3_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"deccc3_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"deccc3_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"deccc3_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"deccc3_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"deccc3_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"deccc3_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"deccc3_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"deccc3_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"deccc3_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"deccc3_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"deccc3_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cc3"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "juncb4":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-4

🌱 Full Name »» `Kota NEET UG 2024 CB-4`
🌀 Start At:  14 June, 2023

✅ MONTH »» Jun 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"juncb4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"juncb4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"juncb4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"juncb4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"juncb4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"juncb4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"juncb4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"juncb4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"juncb4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"juncb4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"juncb4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"juncb4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"juncb4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"juncb4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"juncb4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"juncb4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"juncb4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"juncb4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"juncb4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"juncb4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"juncb4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"juncb4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"juncb4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"juncb4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"juncb4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"juncb4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"juncb4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"juncb4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"juncb4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"juncb4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"juncb4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "julcb4":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-4

🌱 Full Name »» `Kota NEET UG 2024 CB-4`
🌀 Start At:  14 June, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julcb4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julcb4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julcb4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julcb4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julcb4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julcb4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julcb4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julcb4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julcb4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julcb4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julcb4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julcb4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julcb4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julcb4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julcb4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julcb4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julcb4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julcb4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julcb4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julcb4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julcb4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julcb4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julcb4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julcb4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julcb4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julcb4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julcb4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julcb4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julcb4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julcb4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julcb4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augcb4":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-4

🌱 Full Name »» `Kota NEET UG 2024 CB-4`
🌀 Start At:  14 June, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augcb4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augcb4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augcb4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augcb4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augcb4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augcb4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augcb4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augcb4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augcb4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augcb4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augcb4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augcb4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augcb4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augcb4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augcb4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augcb4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augcb4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augcb4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augcb4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augcb4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augcb4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augcb4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augcb4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augcb4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augcb4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augcb4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augcb4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augcb4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augcb4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augcb4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augcb4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septcb4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-4

🌱 Full Name »» `Kota NEET UG 2024 CB-4`
🌀 Start At:  14 June, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septcb4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septcb4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septcb4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septcb4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septcb4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septcb4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septcb4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septcb4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septcb4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septcb4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septcb4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septcb4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septcb4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septcb4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septcb4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septcb4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septcb4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septcb4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septcb4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septcb4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septcb4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septcb4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septcb4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septcb4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septcb4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septcb4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septcb4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septcb4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septcb4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septcb4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septcb4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octcb4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-4

🌱 Full Name »» `Kota NEET UG 2024 CB-4`
🌀 Start At:  14 June, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octcb4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octcb4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octcb4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octcb4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octcb4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octcb4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octcb4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octcb4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octcb4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octcb4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octcb4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octcb4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octcb4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octcb4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octcb4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octcb4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octcb4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octcb4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octcb4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octcb4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octcb4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octcb4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octcb4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octcb4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octcb4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octcb4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octcb4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octcb4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octcb4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octcb4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octcb4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novcb4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-4

🌱 Full Name »» `Kota NEET UG 2024 CB-4`
🌀 Start At:  14 June, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novcb4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novcb4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novcb4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novcb4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novcb4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novcb4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novcb4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novcb4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novcb4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novcb4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novcb4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novcb4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novcb4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novcb4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novcb4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novcb4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novcb4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novcb4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novcb4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novcb4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novcb4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novcb4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novcb4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novcb4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novcb4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novcb4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novcb4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novcb4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novcb4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novcb4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novcb4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "deccb4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CB-4

🌱 Full Name »» `Kota NEET UG 2024 CB-4`
🌀 Start At:  14 June, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"deccb4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"deccb4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"deccb4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"deccb4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"deccb4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"deccb4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"deccb4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"deccb4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"deccb4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"deccb4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"deccb4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"deccb4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"deccb4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"deccb4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"deccb4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"deccb4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"deccb4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"deccb4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"deccb4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"deccb4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"deccb4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"deccb4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"deccb4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"deccb4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"deccb4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"deccb4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"deccb4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"deccb4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"deccb4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"deccb4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"deccb4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cb4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "aprcq1":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanyam Batch

🌱 Full Name »» `Sanyam Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Apr 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"aprcq1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"aprcq1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"aprcq1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"aprcq1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"aprcq1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"aprcq1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"aprcq1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"aprcq1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"aprcq1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"aprcq1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"aprcq1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"aprcq1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"aprcq1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"aprcq1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"aprcq1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"aprcq1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"aprcq1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"aprcq1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"aprcq1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"aprcq1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"aprcq1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"aprcq1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"aprcq1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"aprcq1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"aprcq1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"aprcq1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"aprcq1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"aprcq1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"aprcq1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"aprcq1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"aprcq1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )
    elif data == "maycq1":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanyam Batch

🌱 Full Name »» `Sanyam Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» May 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"maycq1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"maycq1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"maycq1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"maycq1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"maycq1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"maycq1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"maycq1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"maycq1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"maycq1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"maycq1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"maycq1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"maycq1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"maycq1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"maycq1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"maycq1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"maycq1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"maycq1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"maycq1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"maycq1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"maycq1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"maycq1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"maycq1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"maycq1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"maycq1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"maycq1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"maycq1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"maycq1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"maycq1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"maycq1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"maycq1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"maycq1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )
    elif data == "juncq1":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanyam Batch

🌱 Full Name »» `Sanyam Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Jun 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"juncq1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"juncq1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"juncq1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"juncq1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"juncq1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"juncq1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"juncq1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"juncq1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"juncq1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"juncq1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"juncq1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"juncq1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"juncq1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"juncq1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"juncq1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"juncq1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"juncq1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"juncq1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"juncq1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"juncq1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"juncq1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"juncq1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"juncq1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"juncq1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"juncq1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"juncq1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"juncq1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"juncq1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"juncq1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"juncq1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"juncq1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "julcq1":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanyam Batch

🌱 Full Name »» `Sanyam Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julcq1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julcq1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julcq1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julcq1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julcq1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julcq1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julcq1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julcq1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julcq1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julcq1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julcq1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julcq1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julcq1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julcq1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julcq1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julcq1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julcq1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julcq1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julcq1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julcq1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julcq1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julcq1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julcq1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julcq1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julcq1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julcq1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julcq1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julcq1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julcq1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julcq1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julcq1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augcq1":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanyam Batch

🌱 Full Name »» `Sanyam Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augcq1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augcq1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augcq1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augcq1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augcq1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augcq1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augcq1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augcq1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augcq1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augcq1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augcq1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augcq1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augcq1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augcq1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augcq1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augcq1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augcq1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augcq1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augcq1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augcq1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augcq1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augcq1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augcq1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augcq1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augcq1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augcq1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augcq1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augcq1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augcq1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augcq1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augcq1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septcq1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanyam Batch

🌱 Full Name »» `Sanyam Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septcq1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septcq1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septcq1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septcq1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septcq1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septcq1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septcq1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septcq1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septcq1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septcq1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septcq1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septcq1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septcq1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septcq1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septcq1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septcq1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septcq1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septcq1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septcq1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septcq1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septcq1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septcq1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septcq1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septcq1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septcq1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septcq1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septcq1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septcq1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septcq1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septcq1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septcq1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octcq1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanyam Batch

🌱 Full Name »» `Sanyam Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octcq1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octcq1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octcq1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octcq1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octcq1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octcq1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octcq1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octcq1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octcq1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octcq1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octcq1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octcq1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octcq1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octcq1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octcq1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octcq1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octcq1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octcq1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octcq1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octcq1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octcq1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octcq1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octcq1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octcq1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octcq1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octcq1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octcq1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octcq1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octcq1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octcq1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octcq1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novcq1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanyam Batch

🌱 Full Name »» `Sanyam Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novcq1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novcq1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novcq1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novcq1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novcq1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novcq1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novcq1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novcq1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novcq1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novcq1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novcq1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novcq1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novcq1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novcq1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novcq1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novcq1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novcq1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novcq1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novcq1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novcq1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novcq1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novcq1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novcq1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novcq1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novcq1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novcq1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novcq1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novcq1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novcq1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novcq1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novcq1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "deccq1":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanyam Batch

🌱 Full Name »» `Sanyam Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"deccq1_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"deccq1_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"deccq1_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"deccq1_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"deccq1_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"deccq1_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"deccq1_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"deccq1_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"deccq1_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"deccq1_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"deccq1_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"deccq1_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"deccq1_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"deccq1_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"deccq1_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"deccq1_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"deccq1_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"deccq1_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"deccq1_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"deccq1_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"deccq1_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"deccq1_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"deccq1_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"deccq1_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"deccq1_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"deccq1_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"deccq1_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"deccq1_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"deccq1_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"deccq1_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"deccq1_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq1"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "aprcq2":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Yash Batch

🌱 Full Name »» `Yash Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Apr 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"aprcq2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"aprcq2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"aprcq2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"aprcq2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"aprcq2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"aprcq2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"aprcq2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"aprcq2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"aprcq2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"aprcq2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"aprcq2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"aprcq2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"aprcq2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"aprcq2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"aprcq2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"aprcq2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"aprcq2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"aprcq2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"aprcq2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"aprcq2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"aprcq2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"aprcq2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"aprcq2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"aprcq2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"aprcq2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"aprcq2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"aprcq2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"aprcq2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"aprcq2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"aprcq2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"aprcq2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )
    elif data == "maycq2":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Yash Batch

🌱 Full Name »» `Yash Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» May 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"maycq2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"maycq2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"maycq2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"maycq2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"maycq2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"maycq2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"maycq2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"maycq2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"maycq2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"maycq2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"maycq2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"maycq2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"maycq2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"maycq2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"maycq2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"maycq2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"maycq2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"maycq2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"maycq2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"maycq2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"maycq2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"maycq2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"maycq2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"maycq2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"maycq2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"maycq2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"maycq2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"maycq2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"maycq2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"maycq2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"maycq2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )
    elif data == "juncq2":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Yash Batch

🌱 Full Name »» `Yash Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Jun 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"juncq2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"juncq2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"juncq2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"juncq2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"juncq2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"juncq2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"juncq2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"juncq2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"juncq2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"juncq2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"juncq2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"juncq2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"juncq2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"juncq2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"juncq2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"juncq2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"juncq2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"juncq2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"juncq2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"juncq2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"juncq2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"juncq2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"juncq2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"juncq2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"juncq2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"juncq2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"juncq2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"juncq2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"juncq2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"juncq2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"juncq2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "julcq2":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Yash Batch

🌱 Full Name »» `Yash Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julcq2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julcq2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julcq2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julcq2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julcq2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julcq2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julcq2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julcq2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julcq2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julcq2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julcq2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julcq2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julcq2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julcq2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julcq2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julcq2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julcq2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julcq2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julcq2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julcq2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julcq2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julcq2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julcq2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julcq2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julcq2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julcq2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julcq2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julcq2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julcq2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julcq2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julcq2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augcq2":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Yash Batch

🌱 Full Name »» `Yash Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augcq2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augcq2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augcq2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augcq2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augcq2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augcq2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augcq2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augcq2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augcq2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augcq2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augcq2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augcq2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augcq2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augcq2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augcq2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augcq2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augcq2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augcq2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augcq2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augcq2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augcq2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augcq2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augcq2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augcq2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augcq2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augcq2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augcq2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augcq2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augcq2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augcq2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augcq2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septcq2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Yash Batch

🌱 Full Name »» `Yash Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septcq2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septcq2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septcq2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septcq2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septcq2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septcq2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septcq2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septcq2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septcq2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septcq2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septcq2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septcq2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septcq2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septcq2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septcq2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septcq2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septcq2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septcq2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septcq2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septcq2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septcq2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septcq2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septcq2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septcq2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septcq2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septcq2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septcq2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septcq2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septcq2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septcq2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septcq2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octcq2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Yash Batch

🌱 Full Name »» `Yash Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octcq2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octcq2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octcq2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octcq2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octcq2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octcq2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octcq2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octcq2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octcq2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octcq2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octcq2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octcq2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octcq2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octcq2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octcq2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octcq2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octcq2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octcq2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octcq2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octcq2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octcq2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octcq2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octcq2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octcq2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octcq2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octcq2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octcq2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octcq2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octcq2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octcq2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octcq2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novcq2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Yash Batch

🌱 Full Name »» `Yash Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novcq2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novcq2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novcq2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novcq2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novcq2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novcq2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novcq2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novcq2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novcq2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novcq2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novcq2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novcq2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novcq2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novcq2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novcq2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novcq2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novcq2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novcq2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novcq2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novcq2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novcq2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novcq2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novcq2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novcq2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novcq2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novcq2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novcq2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novcq2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novcq2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novcq2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novcq2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "deccq2":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Yash Batch

🌱 Full Name »» `Yash Batch for NEET UG 2024`
🌀 Start At:  15 April, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"deccq2_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"deccq2_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"deccq2_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"deccq2_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"deccq2_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"deccq2_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"deccq2_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"deccq2_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"deccq2_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"deccq2_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"deccq2_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"deccq2_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"deccq2_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"deccq2_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"deccq2_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"deccq2_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"deccq2_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"deccq2_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"deccq2_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"deccq2_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"deccq2_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"deccq2_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"deccq2_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"deccq2_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"deccq2_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"deccq2_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"deccq2_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"deccq2_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"deccq2_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"deccq2_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"deccq2_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq2"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "maycq4":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Prerna Batch

🌱 Full Name »» `Prerna Batch NEET UG 2024`
🌀 Start At:  30 May, 2023

✅ MONTH »» May 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [   InlineKeyboardButton("30", callback_data=f"maycq4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"maycq4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )
    elif data == "juncq4":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Prerna Batch

🌱 Full Name »» `Prerna Batch NEET UG 2024`
🌀 Start At:  30 May, 2023

✅ MONTH »» Jun 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"juncq4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"juncq4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"juncq4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"juncq4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"juncq4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"juncq4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"juncq4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"juncq4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"juncq4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"juncq4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"juncq4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"juncq4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"juncq4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"juncq4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"juncq4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"juncq4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"juncq4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"juncq4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"juncq4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"juncq4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"juncq4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"juncq4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"juncq4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"juncq4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"juncq4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"juncq4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"juncq4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"juncq4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"juncq4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"juncq4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"juncq4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "julcq4":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Prerna Batch

🌱 Full Name »» `Prerna Batch NEET UG 2024`
🌀 Start At:  30 May, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julcq4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julcq4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julcq4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julcq4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julcq4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julcq4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julcq4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julcq4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julcq4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julcq4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julcq4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julcq4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julcq4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julcq4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julcq4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julcq4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julcq4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julcq4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julcq4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julcq4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julcq4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julcq4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julcq4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julcq4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julcq4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julcq4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julcq4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julcq4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julcq4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julcq4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julcq4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augcq4":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Prerna Batch

🌱 Full Name »» `Prerna Batch NEET UG 2024`
🌀 Start At:  30 May, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augcq4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augcq4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augcq4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augcq4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augcq4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augcq4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augcq4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augcq4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augcq4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augcq4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augcq4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augcq4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augcq4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augcq4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augcq4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augcq4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augcq4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augcq4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augcq4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augcq4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augcq4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augcq4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augcq4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augcq4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augcq4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augcq4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augcq4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augcq4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augcq4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augcq4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augcq4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septcq4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Prerna Batch

🌱 Full Name »» `Prerna Batch NEET UG 2024`
🌀 Start At:  30 May, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septcq4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septcq4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septcq4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septcq4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septcq4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septcq4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septcq4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septcq4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septcq4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septcq4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septcq4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septcq4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septcq4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septcq4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septcq4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septcq4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septcq4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septcq4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septcq4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septcq4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septcq4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septcq4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septcq4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septcq4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septcq4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septcq4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septcq4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septcq4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septcq4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septcq4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septcq4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octcq4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Prerna Batch

🌱 Full Name »» `Prerna Batch NEET UG 2024`
🌀 Start At:  30 May, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octcq4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octcq4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octcq4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octcq4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octcq4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octcq4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octcq4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octcq4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octcq4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octcq4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octcq4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octcq4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octcq4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octcq4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octcq4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octcq4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octcq4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octcq4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octcq4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octcq4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octcq4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octcq4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octcq4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octcq4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octcq4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octcq4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octcq4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octcq4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octcq4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octcq4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octcq4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novcq4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Prerna Batch

🌱 Full Name »» `Prerna Batch NEET UG 2024`
🌀 Start At:  30 May, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novcq4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novcq4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novcq4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novcq4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novcq4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novcq4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novcq4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novcq4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novcq4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novcq4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novcq4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novcq4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novcq4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novcq4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novcq4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novcq4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novcq4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novcq4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novcq4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novcq4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novcq4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novcq4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novcq4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novcq4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novcq4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novcq4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novcq4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novcq4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novcq4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novcq4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novcq4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "deccq4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Prerna Batch

🌱 Full Name »» `Prerna Batch NEET UG 2024`
🌀 Start At:  30 May, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"deccq4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"deccq4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"deccq4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"deccq4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"deccq4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"deccq4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"deccq4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"deccq4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"deccq4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"deccq4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"deccq4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"deccq4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"deccq4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"deccq4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"deccq4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"deccq4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"deccq4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"deccq4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"deccq4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"deccq4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"deccq4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"deccq4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"deccq4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"deccq4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"deccq4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"deccq4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"deccq4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"deccq4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"deccq4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"deccq4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"deccq4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "juncq8":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Kartavya Batch

🌱 Full Name »» `Kartavya Batch for NEET 2024`
🌀 Start At:  28 June, 2023

✅ MONTH »» Jun 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        
        [
            InlineKeyboardButton("28", callback_data=f"juncq8_{button_number + 27}"),
            InlineKeyboardButton("29", callback_data=f"juncq8_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"juncq8_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"juncq8_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq8"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
                ]
    )
    )        
    elif data == "julcq8":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Kartavya Batch

🌱 Full Name »» `Kartavya Batch for NEET 2024`
🌀 Start At:  28 June, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julcq8_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julcq8_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julcq8_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julcq8_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julcq8_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julcq8_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julcq8_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julcq8_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julcq8_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julcq8_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julcq8_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julcq8_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julcq8_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julcq8_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julcq8_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julcq8_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julcq8_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julcq8_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julcq8_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julcq8_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julcq8_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julcq8_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julcq8_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julcq8_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julcq8_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julcq8_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julcq8_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julcq8_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julcq8_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julcq8_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julcq8_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq8"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augcq8":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Kartavya Batch

🌱 Full Name »» `Kartavya Batch for NEET 2024`
🌀 Start At:  28 June, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augcq8_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augcq8_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augcq8_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augcq8_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augcq8_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augcq8_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augcq8_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augcq8_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augcq8_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augcq8_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augcq8_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augcq8_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augcq8_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augcq8_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augcq8_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augcq8_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augcq8_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augcq8_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augcq8_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augcq8_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augcq8_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augcq8_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augcq8_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augcq8_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augcq8_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augcq8_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augcq8_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augcq8_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augcq8_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augcq8_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augcq8_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq8"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septcq8":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Kartavya Batch

🌱 Full Name »» `Kartavya Batch for NEET 2024`
🌀 Start At:  28 June, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septcq8_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septcq8_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septcq8_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septcq8_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septcq8_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septcq8_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septcq8_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septcq8_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septcq8_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septcq8_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septcq8_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septcq8_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septcq8_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septcq8_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septcq8_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septcq8_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septcq8_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septcq8_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septcq8_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septcq8_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septcq8_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septcq8_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septcq8_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septcq8_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septcq8_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septcq8_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septcq8_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septcq8_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septcq8_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septcq8_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septcq8_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq8"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octcq8":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Kartavya Batch

🌱 Full Name »» `Kartavya Batch for NEET 2024`
🌀 Start At:  28 June, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octcq8_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octcq8_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octcq8_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octcq8_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octcq8_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octcq8_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octcq8_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octcq8_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octcq8_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octcq8_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octcq8_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octcq8_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octcq8_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octcq8_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octcq8_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octcq8_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octcq8_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octcq8_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octcq8_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octcq8_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octcq8_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octcq8_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octcq8_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octcq8_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octcq8_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octcq8_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octcq8_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octcq8_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octcq8_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octcq8_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octcq8_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq8"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novcq8":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Kartavya Batch

🌱 Full Name »» `Kartavya Batch for NEET 2024`
🌀 Start At:  28 June, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novcq8_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novcq8_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novcq8_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novcq8_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novcq8_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novcq8_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novcq8_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novcq8_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novcq8_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novcq8_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novcq8_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novcq8_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novcq8_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novcq8_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novcq8_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novcq8_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novcq8_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novcq8_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novcq8_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novcq8_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novcq8_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novcq8_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novcq8_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novcq8_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novcq8_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novcq8_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novcq8_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novcq8_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novcq8_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novcq8_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novcq8_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq8"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "deccq8":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Kartavya Batch

🌱 Full Name »» `Kartavya Batch for NEET 2024`
🌀 Start At:  28 June, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"deccq8_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"deccq8_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"deccq8_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"deccq8_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"deccq8_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"deccq8_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"deccq8_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"deccq8_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"deccq8_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"deccq8_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"deccq8_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"deccq8_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"deccq8_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"deccq8_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"deccq8_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"deccq8_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"deccq8_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"deccq8_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"deccq8_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"deccq8_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"deccq8_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"deccq8_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"deccq8_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"deccq8_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"deccq8_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"deccq8_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"deccq8_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"deccq8_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"deccq8_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"deccq8_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"deccq8_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq8"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "julcq11":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanshodhan Batch

🌱 Full Name »» `Sanshodhan Batch for NEET 2024`
🌀 Start At:  03 July, 2023
✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"julcq11_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"julcq11_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"julcq11_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"julcq11_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"julcq11_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"julcq11_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"julcq11_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"julcq11_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"julcq11_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"julcq11_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"julcq11_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"julcq11_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"julcq11_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"julcq11_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"julcq11_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"julcq11_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"julcq11_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"julcq11_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julcq11_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julcq11_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julcq11_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julcq11_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julcq11_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julcq11_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julcq11_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julcq11_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julcq11_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julcq11_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julcq11_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julcq11_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julcq11_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq11"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augcq11":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanshodhan Batch

🌱 Full Name »» `Sanshodhan Batch for NEET 2024`
🌀 Start At:  03 July, 2023
✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augcq11_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augcq11_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augcq11_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augcq11_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augcq11_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augcq11_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augcq11_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augcq11_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augcq11_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augcq11_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augcq11_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augcq11_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augcq11_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augcq11_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augcq11_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augcq11_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augcq11_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augcq11_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augcq11_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augcq11_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augcq11_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augcq11_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augcq11_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augcq11_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augcq11_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augcq11_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augcq11_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augcq11_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augcq11_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augcq11_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augcq11_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq11"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septcq11":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanshodhan Batch

🌱 Full Name »» `Sanshodhan Batch for NEET 2024`
🌀 Start At:  03 July, 2023
✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septcq11_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septcq11_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septcq11_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septcq11_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septcq11_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septcq11_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septcq11_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septcq11_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septcq11_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septcq11_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septcq11_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septcq11_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septcq11_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septcq11_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septcq11_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septcq11_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septcq11_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septcq11_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septcq11_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septcq11_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septcq11_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septcq11_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septcq11_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septcq11_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septcq11_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septcq11_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septcq11_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septcq11_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septcq11_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septcq11_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septcq11_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq11"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octcq11":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanshodhan Batch

🌱 Full Name »» `Sanshodhan Batch for NEET 2024`
🌀 Start At:  03 July, 2023
✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octcq11_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octcq11_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octcq11_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octcq11_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octcq11_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octcq11_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octcq11_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octcq11_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octcq11_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octcq11_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octcq11_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octcq11_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octcq11_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octcq11_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octcq11_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octcq11_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octcq11_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octcq11_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octcq11_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octcq11_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octcq11_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octcq11_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octcq11_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octcq11_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octcq11_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octcq11_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octcq11_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octcq11_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octcq11_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octcq11_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octcq11_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq11"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novcq11":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanshodhan Batch

🌱 Full Name »» `Sanshodhan Batch for NEET 2024`
🌀 Start At:  03 July, 2023
✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novcq11_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novcq11_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novcq11_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novcq11_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novcq11_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novcq11_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novcq11_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novcq11_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novcq11_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novcq11_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novcq11_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novcq11_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novcq11_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novcq11_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novcq11_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novcq11_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novcq11_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novcq11_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novcq11_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novcq11_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novcq11_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novcq11_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novcq11_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novcq11_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novcq11_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novcq11_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novcq11_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novcq11_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novcq11_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novcq11_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novcq11_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq11"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "deccq11":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Sanshodhan Batch

🌱 Full Name »» `Sanshodhan Batch for NEET 2024`
🌀 Start At:  03 July, 2023
✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"deccq11_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"deccq11_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"deccq11_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"deccq11_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"deccq11_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"deccq11_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"deccq11_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"deccq11_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"deccq11_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"deccq11_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"deccq11_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"deccq11_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"deccq11_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"deccq11_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"deccq11_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"deccq11_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"deccq11_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"deccq11_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"deccq11_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"deccq11_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"deccq11_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"deccq11_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"deccq11_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"deccq11_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"deccq11_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"deccq11_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"deccq11_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"deccq11_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"deccq11_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"deccq11_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"deccq11_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq11"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    ) 
    elif data == "julcq13":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Pahal Batch

🌱 Full Name »» `Pahal Batch for NEET 2024`
🌀 Start At:  31 July, 2023
✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [    
            InlineKeyboardButton("31", callback_data=f"julcq13_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq13"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augcq13":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Pahal Batch

🌱 Full Name »» `Pahal Batch for NEET 2024`
🌀 Start At:  31 July, 2023
✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augcq13_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augcq13_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augcq13_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augcq13_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augcq13_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augcq13_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augcq13_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augcq13_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augcq13_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augcq13_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augcq13_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augcq13_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augcq13_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augcq13_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augcq13_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augcq13_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augcq13_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augcq13_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augcq13_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augcq13_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augcq13_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augcq13_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augcq13_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augcq13_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augcq13_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augcq13_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augcq13_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augcq13_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augcq13_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augcq13_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augcq13_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq13"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septcq13":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Pahal Batch

🌱 Full Name »» `Pahal Batch for NEET 2024`
🌀 Start At:  31 July, 2023
✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septcq13_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septcq13_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septcq13_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septcq13_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septcq13_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septcq13_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septcq13_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septcq13_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septcq13_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septcq13_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septcq13_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septcq13_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septcq13_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septcq13_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septcq13_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septcq13_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septcq13_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septcq13_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septcq13_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septcq13_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septcq13_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septcq13_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septcq13_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septcq13_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septcq13_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septcq13_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septcq13_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septcq13_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septcq13_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septcq13_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septcq13_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq13"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octcq13":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Pahal Batch

🌱 Full Name »» `Pahal Batch for NEET 2024`
🌀 Start At:  31 July, 2023
✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octcq13_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octcq13_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octcq13_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octcq13_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octcq13_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octcq13_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octcq13_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octcq13_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octcq13_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octcq13_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octcq13_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octcq13_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octcq13_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octcq13_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octcq13_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octcq13_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octcq13_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octcq13_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octcq13_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octcq13_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octcq13_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octcq13_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octcq13_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octcq13_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octcq13_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octcq13_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octcq13_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octcq13_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octcq13_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octcq13_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octcq13_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq13"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novcq13":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Pahal Batch

🌱 Full Name »» `Pahal Batch for NEET 2024`
🌀 Start At:  31 July, 2023
✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novcq13_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novcq13_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novcq13_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novcq13_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novcq13_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novcq13_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novcq13_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novcq13_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novcq13_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novcq13_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novcq13_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novcq13_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novcq13_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novcq13_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novcq13_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novcq13_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novcq13_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novcq13_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novcq13_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novcq13_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novcq13_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novcq13_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novcq13_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novcq13_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novcq13_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novcq13_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novcq13_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novcq13_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novcq13_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novcq13_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novcq13_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq13"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "deccq13":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» Pahal Batch

🌱 Full Name »» `Pahal Batch for NEET 2024`
🌀 Start At:  31 July, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"deccq13_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"deccq13_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"deccq13_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"deccq13_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"deccq13_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"deccq13_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"deccq13_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"deccq13_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"deccq13_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"deccq13_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"deccq13_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"deccq13_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"deccq13_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"deccq13_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"deccq13_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"deccq13_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"deccq13_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"deccq13_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"deccq13_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"deccq13_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"deccq13_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"deccq13_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"deccq13_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"deccq13_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"deccq13_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"deccq13_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"deccq13_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"deccq13_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"deccq13_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"deccq13_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"deccq13_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"cq13"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    ) 
    elif data == "julce4":
        
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CE-4

🌱 Full Name »» `Kota NEET UG 2024 CE-4`
🌀 Start At:  18 July, 2023

✅ MONTH »» Jul 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [   InlineKeyboardButton("18", callback_data=f"julce4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"julce4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"julce4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"julce4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"julce4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"julce4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"julce4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"julce4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"julce4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"julce4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"julce4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"julce4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"julce4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"julce4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"ce4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "augce4":
        # Handle crx case
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CE-4

🌱 Full Name »» `Kota NEET UG 2024 CE-4`
🌀 Start At:  18 July, 2023

✅ MONTH »» Aug 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"augce4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"augce4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"augce4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"augce4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"augce4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"augce4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"augce4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"augce4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"augce4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"augce4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"augce4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"augce4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"augce4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"augce4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"augce4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"augce4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"augce4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"augce4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"augce4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"augce4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"augce4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"augce4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"augce4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"augce4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"augce4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"augce4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"augce4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"augce4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"augce4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"augce4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"augce4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"ce4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "septce4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CE-4

🌱 Full Name »» `Kota NEET UG 2024 CE-4`
🌀 Start At:  18 July, 2023

✅ MONTH »» Sept 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"septce4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"septce4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"septce4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"septce4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"septce4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"septce4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"septce4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"septce4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"septce4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"septce4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"septce4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"septce4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"septce4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"septce4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"septce4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"septce4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"septce4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"septce4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"septce4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"septce4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"septce4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"septce4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"septce4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"septce4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"septce4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"septce4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"septce4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"septce4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"septce4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"septce4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"septce4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"ce4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "octce4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CE-4

🌱 Full Name »» `Kota NEET UG 2024 CE-4`
🌀 Start At:  18 July, 2023

✅ MONTH »» Oct 2023

""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"octce4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"octce4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"octce4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"octce4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"octce4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"octce4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"octce4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"octce4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"octce4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"octce4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"octce4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"octce4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"octce4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"octce4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"octce4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"octce4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"octce4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"octce4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"octce4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"octce4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"octce4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"octce4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"octce4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"octce4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"octce4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"octce4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"octce4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"octce4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"octce4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"octce4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"octce4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"ce4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    elif data == "novce4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CE-4

🌱 Full Name »» `Kota NEET UG 2024 CE-4`
🌀 Start At:  18 July, 2023

✅ MONTH »» nov 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"novce4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"novce4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"novce4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"novce4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"novce4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"novce4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"novce4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"novce4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"novce4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"novce4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"novce4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"novce4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"novce4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"novce4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"novce4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"novce4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"novce4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"novce4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"novce4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"novce4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"novce4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"novce4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"novce4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"novce4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"novce4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"novce4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"novce4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"novce4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"novce4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"novce4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"novce4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"ce4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )    
    elif data == "decce4":
        button_number = 1
        await query.message.edit_text(
            text = """🌀 BATCH NAME »» CE-4

🌱 Full Name »» `Kota NEET UG 2024 CE-4`
🌀 Start At:  18 July, 2023

✅ MONTH »» Dec 2023
""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("1", callback_data=f"decce4_{button_number}"),
            InlineKeyboardButton("2", callback_data=f"decce4_{button_number + 1}"),
            InlineKeyboardButton("3", callback_data=f"decce4_{button_number + 2}"),
            InlineKeyboardButton("4", callback_data=f"decce4_{button_number + 3}"),
        ],
        [
            InlineKeyboardButton("5", callback_data=f"decce4_{button_number + 4}"),
            InlineKeyboardButton("6", callback_data=f"decce4_{button_number + 5}"),
            InlineKeyboardButton("7", callback_data=f"decce4_{button_number + 6}"),
            InlineKeyboardButton("8", callback_data=f"decce4_{button_number + 7}"),
        ],
        [
            InlineKeyboardButton("9", callback_data=f"decce4_{button_number  + 8}"),
            InlineKeyboardButton("10", callback_data=f"decce4_{button_number + 9}"),
            InlineKeyboardButton("11", callback_data=f"decce4_{button_number + 10}"),
            InlineKeyboardButton("12", callback_data=f"decce4_{button_number + 11}"),
        ],
        [
            InlineKeyboardButton("13", callback_data=f"decce4_{button_number + 12}"),
            InlineKeyboardButton("14", callback_data=f"decce4_{button_number + 13}"),
            InlineKeyboardButton("15", callback_data=f"decce4_{button_number + 14}"),
            InlineKeyboardButton("16", callback_data=f"decce4_{button_number + 15}"),
        ],
        [
            InlineKeyboardButton("17", callback_data=f"decce4_{button_number + 16}"),
            InlineKeyboardButton("18", callback_data=f"decce4_{button_number + 17}"),
            InlineKeyboardButton("19", callback_data=f"decce4_{button_number + 18}"),
            InlineKeyboardButton("20", callback_data=f"decce4_{button_number + 19}"),
        ],
        [
            InlineKeyboardButton("21", callback_data=f"decce4_{button_number + 20}"),
            InlineKeyboardButton("22", callback_data=f"decce4_{button_number + 21}"),
            InlineKeyboardButton("23", callback_data=f"decce4_{button_number + 22}"),
            InlineKeyboardButton("24", callback_data=f"decce4_{button_number + 23}"),
        ],
        [
            InlineKeyboardButton("25", callback_data=f"decce4_{button_number + 24}"),
            InlineKeyboardButton("26", callback_data=f"decce4_{button_number + 25}"),
            InlineKeyboardButton("27", callback_data=f"decce4_{button_number + 26}"),
            InlineKeyboardButton("28", callback_data=f"decce4_{button_number + 27}"),
        ],
        [
            InlineKeyboardButton("29", callback_data=f"decce4_{button_number + 28}"),
            InlineKeyboardButton("30", callback_data=f"decce4_{button_number + 29}"),
            InlineKeyboardButton("31", callback_data=f"decce4_{button_number + 30}"),
        ],
        [   
            InlineKeyboardButton("Back", callback_data=f"ce4"),
            InlineKeyboardButton("Close", callback_data=f"close"),
        ],
        ]
    )
    )
    
