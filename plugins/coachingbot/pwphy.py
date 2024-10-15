
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=95656)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    phypw_info = [] 
    if data == "pw_phy":
      phypw_info = [
        f'''  
🌱**[BASIC MATHS ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY1NTA2MjY0NDMwOTI1OTItNjU2MDY0NTc1NTQ4NjQzMg)**

🌱**[VECTOR ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY1NjE2NDc2ODY3MjU4MTYtNjU2NjY1NzM0MjkyMjczNg)**

🌱**[UNIT MEASUREMENT AND ERROR ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY1Njc2NTkyNzQxNjIxMjAtNjU3NzY3ODU4NjU1NTk2MA)**

🌱**[MOTION IN 1D ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY1Nzg2ODA1MTc3OTUzNDQtNjU5MjcwNzU1NTE0NjcyMA)**

🌱**[MOTION IN 2D ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY1OTM3MDk0ODYzODYxMDQtNjYwMTcyNDkzNjMwMTE3Ng)**

🌱**[NLM ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2MDI3MjY4Njc1NDA1NjAtNjYxMzc0ODExMTE3Mzc4NA)**
 
🌱**[WPE ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2MTQ3NTAwNDI0MTMxNjgtNjYyMjc2NTQ5MjMyODI0MA)**

🌱**[COM ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2MjM3Njc0MjM1Njc2MjQtNjYyOTc3OTAxMTAwMzkyOA)**

🌱**[ROTATIONAL MOTION ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2MzA3ODA5NDIyNDMzMTItNjY0MDgwMDI1NDYzNzE1Mg)**

🌱**[GRAVITATION ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2NDE4MDIxODU4NzY1MzYtNjY0NzgxMzc3MzMxMjg0MA)**

🌱**[MECHANICAL PROPERTIES OF SOLIDS ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2NDg4MTU3MDQ1NTIyMjQtNjY1MTgyMTQ5ODI3MDM3Ng)**

🌱**[MECHANICAL PROPERTIES OF FLUIDS ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2NTI4MjM0Mjk1MDk3NjAtNjY2Mjg0Mjc0MTkwMzYwMA)**

🌱**[THERMAL PROPERTIES OF MATTER ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2NjM4NDQ2NzMxNDI5ODQtNjY2OTg1NjI2MDU3OTI4OA)**

🌱**[THERMODYNAMICS AND KTG ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2NzA4NTgxOTE4MTg2NzItNjY3Nzg3MTcxMDQ5NDM2MA)**

🌱**[SHM ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2Nzg4NzM2NDE3MzM3NDQtNjY4NDg4NTIyOTE3MDA0OA)**

🌱**[WAVE MOTION ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2ODU4ODcxNjA0MDk0MzItNjY5MjkwMDY3OTA4NTEyMA)**

🌱**[ELECTRIC CHARGES AND FLUIDS ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY2OTM5MDI2MTAzMjQ1MDQtNjcwMzkyMTkyMjcxODM0NA)**

🌱**[ELECTROSTATIC POTENTIAL AND CAPACITANCE ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3MDQ5MjM4NTM5NTc3MjgtNjcxMjkzOTMwMzg3MjgwMA)**

🌱**[CURRENT ELECTRICITY ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3MTM5NDEyMzUxMTIxODQtNjcyMjk1ODYxNjI2NjY0MA)**

🌱**[MEC ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3MjM5NjA1NDc1MDYwMjQtNjczMTk3NTk5NzQyMTA5Ng)**

🌱**[MAGNETISM AND MATTER ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3MzI5Nzc5Mjg2NjA0ODAtNjczNjk4NTY1MzYxODAxNg)**

🌱**[EMI ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3Mzc5ODc1ODQ4NTc0MDAtNjc0Mjk5NzI0MTA1NDMyMA)**

🌱**[AC ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3NDM5OTkxNzIyOTM3MDQtNjc0ODAwNjg5NzI1MTI0MA)**

🌱**[EMW ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3NDkwMDg4Mjg0OTA2MjQtNjc1MTAxMjY5MDk2OTM5Mg)**

🌱**[RAY OPTICS ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3NTIwMTQ2MjIyMDg3NzYtNjc2MDAzMDA3MjEyMzg0OA)**

🌱**[WAVE OPTICS ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3NjEwMzIwMDMzNjMyMzItNjc2NTAzOTcyODMyMDc2OA)**

🌱**[DUAL NATURE OF MATTER ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3NjYwNDE2NTk1NjAxNTItNjc2OTA0NzQ1MzI3ODMwNA)**

🌱**[ATOMS ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3NzAwNDkzODQ1MTc2ODgtNjc3MjA1MzI0Njk5NjQ1Ng)**

🌱**[NUCLEAR PHYSICS ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3NzMwNTUxNzgyMzU4NDAtNjc3NjA2MDk3MTk1Mzk5Mg)**

🌱**[SEMICONDUCTOR ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3NzcwNjI5MDMxOTMzNzYtNjc4MjA3MjU1OTM5MDI5Ng)**

🌱**[COMPLETE NOTES AND DPP ✘ MR SIR PHYSICS YAKEEN 2.0 2023](https://t.me/{BOT_USERNM}?start=Z2V0LTY3ODMwNzQ0OTA2Mjk2ODAtNjgxNDEzNDM1OTA1MDU4NA)**

        ''',
                

        
    ]
    
    # Send each piece of information as a separate message
    for info in phypw_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.1)

        await query.answer("PW PHYSICS LECTURES SENT SUCESSFULLY✅", show_alert=True)
