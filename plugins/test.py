import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM



@Bot.on_message(filters.command('test') & filters.group, group=434)
async def help(bot: Bot, message: Message):
 test_info = [] 
 
 test_info = [ 
 f'''
🔮**NEET 2021 **

**[GOAL DPP ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTE5NTI3NjM5ODU1NTk0MTYtMTk4MjgyMTkyMjc0MDkzNg)**

**[BTS FOR NEET 2021 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIyMTMyNjYxMDc3OTkyNTYtMjIzNDMwNjY2MzgyNjMyMA)** 

**[CTT FOR NEET 2021 PART 1 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIyMzUzMDg1OTUwNjU3MDQtMjI2MDM1Njg3NjA1MDMwNA)** 

**[CTT FOR NEET 2021 PART 2  ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIyNjEzNTg4MDcyODk2ODgtMjI4ODQxMDk1MDc1MzA1Ng)**

**[TARGET NEET 2021  ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIyODk0MTI4ODE5OTI0NDAtMjMxMDQ1MzQzODAxOTUwNA)**

**[ALFTS 2021 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIzMzc1MDU1ODE0ODI4NzItMjM0NzUyNDg5Mzg3NjcxMg)** 

**[SRBTS FOR NEET 2021 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIzMTE0NTUzNjkyNTg4ODgtMjMzNjUwMzY1MDI0MzQ4OA)** ''',

f'''🔮**NEET 2022**

**[GOAL MAJOR ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTE5ODY4Mjk2NDc2OTg0NzItMjAwMjg2MDU0NzUyODYxNg)**

**[GOAL SPOT TEST SERIES ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTEyNDEzOTI4MDU1OTY3NzYtMTI3MzQ1NDYwNTI1NzA2NA)**

**[CHEMISTRY TOPIC TEST SERIES ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIxMDkwNjUyNTg5MDMzMjAtMjExOTA4NDU3MTI5NzE2MA)** 

**[BTS FOR NEET 2022 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIxOTcyMzUyMDc5NjkxMTItMjIxMjI2NDE3NjU1OTg3Mg)** 

**[PTT FOR NEET 2022 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIxMzIxMDk2Nzc0MDkxNTItMjE1OTE2MTgyMDg3MjUyMA)** 

**[CTT FOR NEET 2022 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIxNjAxNjM3NTIxMTE5MDQtMjE4NTIxMjAzMzA5NjUwNA)** 

**[CPT FOR NEET 2022 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIxODYyMTM5NjQzMzU4ODgtMjE5NjIzMzI3NjcyOTcyOA)**

**[NBTS 2022 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIzNDg1MjY4MjUxMTYwOTYtMjM1OTU0ODA2ODc0OTMyMA)** ''',

f'''🔮**NEET 2023**

**[AITS ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTE5Mjk3MTk1NjcwNTM1ODQtMTk1MTc2MjA1NDMyMDAzMg)**

**[GOAL SPOT TEST SERIES ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTE5MTQ2OTA1OTg0NjI4MjQtMTkyODcxNzYzNTgxNDIwMA)**

**[NTS ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIzNjA1NDk5OTk5ODg3MDQtMjM4MzU5NDQxODQ5NDUzNg)** 

**[BTS ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTIzODQ1OTYzNDk3MzM5MjAtMjQyMDY2NTg3NDM1MTc0NA)** 

**[FLT  PART 01 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI0MjE2Njc4MDU1OTExMjgtMjQ2Mjc0Njk4NjQwNTg3Mg)** 

**[FLT PART 02 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI0NjM3NDg5MTc2NDUyNTYtMjUwNjgzMTk2MDkzODc2OA)** 

**[SBTS ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI1MDc4MzM4OTIxNzgxNTItMjUyODg3NDQ0ODIwNTIxNg)** 

**[RBTS ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI1Mjk4NzYzNzk0NDQ2MDAtMjU0MDg5NzYyMzA3NzgyNA)** 

**[UBT ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI1NDE4OTk1NTQzMTcyMDgtMjU3MDk1NTU2MDI1OTM0NA)** 

**[IPL ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI1NzE5NTc0OTE0OTg3MjgtMjU4MDk3NDg3MjY1MzE4NA)** ''',


f'''🔮**NEET 2024**

**[NTS ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI2MTEwMzI4MDk4MzQ3MDQtMjYyNTA1OTg0NzE4NjA4MA)** 

**[FLT ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI1ODE5NzY4MDM4OTI1NjgtMjYxMDAzMDg3ODU5NTMyMA)** 

**[BTS ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI2MjYwNjE3Nzg0MjU0NjQtMjY1NDExNTg1MzEyODIxNg)** 

**[UBT ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI2NTUxMTc3ODQzNjc2MDAtMjY2MzEzMzIzNDI4MjY3Mg)** 

**[SBTS ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI2NjQxMzUxNjU1MjIwNTYtMjY3MDE0Njc1Mjk1ODM2MA)** 

**[IPL ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTI2NzExNDg2ODQxOTc3NDQtMjY3MzE1MjU0NjY3NjUxMg)** 


 
 
 ''',
f'''
🍀**AAKASH DROPPER **

**[PHASE FT 01 - 07 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTc1MDQ0NjQ5ODI5ODYxNjAtNzUxNzQ5MDA4OTA5ODE1Mg)**

**[PHASE 02 FT01- 05 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTc1MTg0OTIwMjAzMzc1MzYtNzUyOTUxMzI2Mzk3MDc2MA)**

**[PHASE 03 FT01-04 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTc1MzA1MTUxOTUyMTAxNDQtNzUzODUzMDY0NTEyNTIxNg)**

**[PHASE 04 FT01-03 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTc1Mzk1MzI1NzYzNjQ2MDAtNzU0NTU0NDE2MzgwMDkwNA)**

**[PHASE 05 FT 01 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTc1NDY1NDYwOTUwNDAyODgtNzU0ODU0OTk1NzUxOTA1Ng)**

**[AIATS 01 WITH CSS ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTc1NTU1NjM0NzYxOTQ3NDQtNzU2MTU3NTA2MzYzMTA0OA)**

**[POLL TEST 01 ](https://t.me/{BOT_USERNM}?stargoupt=Z2V0LTc1NDk1NTE4ODg3NTg0NDAtNzU1NDU2MTU0NDk1NTM2MA)**

''',
  f''' 🍀UNACADEMY 

**[UAITS  01 AND 02 ](https://t.me/{BOT_USERNM}?startgroup=Z2V0LTc2MzA3MDgzMTkxNDg1NDQtNzYzNDcxNjA0NDEwNjA4MA)**
 ''',
 ]
 
 for info in test_info:
        await message.reply_text(info, disable_web_page_preview=True, parse_mode = ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.2)

        
    
        parse_mode=ParseMode.HTML,
