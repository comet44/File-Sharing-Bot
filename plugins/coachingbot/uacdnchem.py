
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=992)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    chemu_info = [] 
    if data == "un_chem":
      chemu_info = [
        f'''  🔮 **CLASS 11 CHEMISTRY UNACADEMY**

🌱 **[BASICS OF PHYSICAL CHEMISTRY ✘ SANJAY MISHRA SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNzY3NTM3MTYwMzc1NTQ0LTEzNzgwNTYyMjY2NDg3NTM2)**
        
        
🌱**[ MOLE CONCEPT ✘ AKM SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTk1MTgzNDY3NzQxNDgwLTExNTIyMjA5MjUyOTE2MA)**

🌱**[MOLE CONCEPT ✘ AKM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyOTczMDA1Njg3NTQ0MDMyLTEyOTk2MDUwMTA2MDQ5ODY0)**

🌱**[MOLE CONCEPT ✘ TNM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNDMxOTYyODE4Mjc2NjcyLTEyNDQzOTg1OTkzMTQ5Mjgw)**

🌱**[MOLE CONCEPT ✘ SM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNzgxNTY0MTk3NzI2OTIwLTEzODEyNjI0MDY2MTQ3ODI0)**

🌱 **[MOLE CONCEPT ✘ LY SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMjIxNDg0NjM0OTExMjY0LTEzMjMxNTAzOTQ3MzA1MTA0)**


🌱**[ATOMIC STRUCTURE ✘ SS SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTExMzg2OTQ4NTM1NTk5MTYwLTExMzkzOTYyMDU0Mjc0ODQ4)**


🌱**[CHEMICAL EQUILIBRIUM ✘ AKM SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTE4NDE1NDk2MTc5ODc3OTItMTg1NTU3NjY1NTMzOTE2OA)**

🌱**[CHEMICAL EQUILLIBRIUM ✘ SM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzODQ0Njg1ODY1ODA4MTEyLTEzODU3NzEwOTcxOTIwMTA0)**


🌱**[IONIC LEC 1  5 ✘ SM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzODU4NzEyOTAzMTU5NDg4LTEzODYyNzIwNjI4MTE3MDI0)**


🌱**[REDOX ✘ TNM SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU4OTEzNTU2ODc1Nzc5Mi0xMDY4MDU4NzAxMTgzMzQ0)**

🌱**[REDOX ✘ TNM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNTE2MTI1MDQyMzg0OTI4LTEyNTMxMTU0MDEwOTc1Njg4)**

🌱**[REDOX ✘ LY SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMjMyNTA1ODc4NTQ0NDg4LTEzMjM5NTE5Mzk3MjIwMTc2)**


🌱**[SOME BASIC CONCEPT OF INORGANIC CHEMISTRY ✘ RS SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMDMzMTIxNTYxOTA3MDcyLTEzMDQ4MTUwNTMwNDk3ODMy)**


🌱**[PERIODIC TABLE ✘ RD SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTIyMzQzMDY2NjM4MjYzMi0yNDE0NjU0Mjg2OTE1NDQ)**

🌱**[PERIODIC TABLE ✘ RD SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyMzE0NzM2ODYzMjY4NzQ0LTEyMzUyODEwMjUwMzY1MzM2)**

🌱**[PERIODIC TABLE ✘ AB SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTQ5OTk2MzY4ODQ1MjYxNi01MTQ5OTI2NTcwNDMzNzY)**

🌱**[PERIODIC TABLE AB SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyMTk2NTA4OTc3MDIxNDMyLTEyMjI0NTYzMDUxNzI0MTg0)**

🌱**[PERIODIC TABLE ✘ RS SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMDQ5MTUyNDYxNzM3MjE2LTEzMDcxMTk0OTQ5MDAzNjY0)**



🌱**[CHEMICAL BONDING ✘ RD SIR 2024](https://t.me/{BOT_USERNM}?start=Z2V0LTI0MTQ2NTQyODY5MTU0NC0yNzA1MjE0MzQ2MzM2ODA)** 

🌱**[CHEMICAL BONDING ✘ RD SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyMzUzODEyMTgxNjA0NzIwLTEyNDE0OTI5OTg3MjA3MTQ0)**

🌱**[CHEMICAL BONDING ✘ AB SIR 2024](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NTQ4MDQxNTk1ODU1NjgtMTQ3MTgzNjk5MDY1NTA5Ng)**

🌱**[CHEMICAL BONDING ✘ AB SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyMjI1NTY0OTgyOTYzNTY4LTEyMjQ1NjAzNjA3NzUxMjQ4)**

🌱**[CHEMICAL BONDING ✘ RS SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMDcyMTk2ODgwMjQzMDQ4LTEzMDg2MjIzOTE3NTk0NDI0)**



🌱**[S BLOCK ✘ RD SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTI3MTUyMzM2NTg3MzA2NC0yNzY1MzMwMjIwNjk5ODQ)**

🌱**[S BLOCK ✘ AB SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTE0OTA4NzM2ODQyMDMzOTItMTQ5MTg3NTYxNTQ0Mjc3Ng)**


🌱**[P BLOCK ✘ RD SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTkwOTc1MzU2NTM2MDY3Mi05MjU3ODQ0NjUxOTA4MTY)**

🌱**[P BLOCK ✘ RD SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNDE1OTMxOTE4NDQ2NTI4LTEyNDMwOTYwODg3MDM3Mjg4)**

🌱**[P BLOCK ✘ AB SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NzI4Mzg5MjE4OTQ0ODAtMTQ4OTg3MTc1Mjk2NDAwOA)**

🌱**[P BLOCK  ✘ AB SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyMjQ2NjA1NTM4OTkwNjMyLTEyMjUwNjEzMjYzOTQ4MTY4)**


🌱**[D & F BLOCK ✘ RD SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTkyNjc4NjM5NjQzMDIwMC05MzA3OTQxMjEzODc3MzY)**


🌱**[HYDROGEN AND ITS COMPOUND ✘ AB SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTE0OTI4Nzc5OTk4NzA5NjAtMTQ5NTg4MzM0MDQwMDMxMg)**

''',
          f'''


🌱 **[BASIC CONCEPTs OF OC   ✘ SKC SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTE2NzgyMzQ4MjU5NjgyMDAtMTY4MTI0MDYxOTY4NjM1Mg)** 



        
🌱 **[NOMENCLATURE ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTI3NzUzNDk1MzMwOTM2OC0yODY1NTIzMzQ0NjM4MjQ)**

🌱 **[NOMENCLATURE ✘ YSY SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNjM2MzU2NzkxMTExMDA4LTEyNjQzMzcwMzA5Nzg2Njk2)**

🌱 **[NOMENCLATURE ✘ ACID SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU0NjA1MjUyNTQ2NDI4MC01NTUwNjk5MDY2MTg3MzY)** 

🌱 **[NOMENCLATURE ✘ SKC SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTE2ODIyNDI1NTA5MjU3MzYtMTY4NzI1MjIwNzEyMjY1Ng)**

🌱 **[NOMENCLATURE ✘ SKC SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNzQzNTYzNDMzNzI1MDk2LTEyNzU0NTg0Njc3MzU4MzIw)**




🌱**[CLASSIFICATION & NOMENCLATURE ✘ ACID SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTExMzk0OTYzOTg1NTE0MjMyLTExNDE2MDA0NTQxNTQxMjk2)**

🌱**[CLASSIFICATION & NOMENCLATURE ✘ ACID SIR HINDI 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTExNzYyNjcyNzUwMzY4MTYwLTExNzgzNzEzMzA2Mzk1MjI0)**

🌱 **[CLASSIFICATION & NOMENCLATURE ✘ SD SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNjY1MzQwMTczOTU4Mzc2LTEzNjk1Mzk4MTExMTM5ODk2)**

🌱 **[CLASSIFICATION & NOMENCLATURE ✘ PRADIP KUMAR SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMzYyNzU2OTM5NjY0NDA4LTEzMzk1ODIwNjcwNTY0MDgw)**


🌱 **[ISOMERISM  ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTI4NzU1NDI2NTcwMzIwOC0zMDg1OTQ4MjE3MzAyNzI)**

🌱 **[ISOMERISM ✘ YSY SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNjQ0MzcyMjQxMDI2MDgwLTEyNjYxNDA1MDcyMDk1NjA4)**

🌱 **[ISOMERSIM ✘ ACID SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTgyNTU5MTM0MTI1MjQxNi04NDI2MjQxNzIzMjE5NDQ)**

🌱 **[ISOMERISM  ✘ SKC SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTE2ODgyNTQxMzgzNjIwNDAtMTcwMzI4MzEwNjk1MjgwMA)**

🌱 **[ISOMERISM ✘ SKC SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNzU1NTg2NjA4NTk3NzA0LTEyNzY5NjEzNjQ1OTQ5MDgw)**

🌱 **[ISOMERISM ✘ ACID SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTExNDE3MDA2NDcyNzgwNjgwLTExNDQ1MDYwNTQ3NDgzNDMy)**

🌱 **[ISOMERISM ✘ ACID SIR HINDI 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTExNzg0NzE1MjM3NjM0NjA4LTExODA4NzYxNTg3Mzc5ODI0)**

🌱 **[ISOMERISM ✘ SD SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNjk2NDAwMDQyMzc5MjgwLTEzNzE4NDQyNTI5NjQ1NzI4)**

🌱 **[ISOMERISM ✘ PK SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMzk2ODIyNjAxODAzNDY0LTEzNDE2ODYxMjI2NTkxMTQ0)**


🌱 **[GOC ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTMwOTU5Njc1Mjk2OTY1Ni0zMjk2MzUzNzc3NTczMzY)**

🌱 **[GOC ✘ YSY SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNjYyNDA3MDAzMzM0OTkyLTEyNzAwNDgwMzkwNDMxNTg0)**

🌱 **[GOC ✘ ACID SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTEwMDg5NDQ3NTgwNTk2ODgtMTAyODk4MzM4Mjg0NzM2OA)**

🌱 **[GOC ✘ SKC SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTIwOTEwMzA0OTY1OTQ0MDgtMjEwNzA2MTM5NjQyNDU1Mg)**

🌱 **[GOC ✘ ACID SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTExNDQ2MDYyNDc4NzIyODE2LTExNDgxMTMwMDcyMTAxMjU2)**

🌱 **[GOC ✘ ACID SIR HINDI 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTExODA5NzYzNTE4NjE5MjA4LTExODQwODIzMzg3MDQwMTEy)**

🌱 **[GOC ✘ SD SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNzE5NDQ0NDYwODg1MTEyLTEzNzM4NDgxMTU0NDMzNDA4)**

🌱 **[GOC ✘ PK SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNDE3ODYzMTU3ODMwNTI4LTEzNDM1ODk3OTIwMTM5NDQw)**


🌱 **[TAUTOMERISM ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTMzMDYzNzMwODk5NjcyMC0zMzE2MzkyNDAyMzYxMDQ)**


🌱 **[REACTION MECHANISM ✘ ACID SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTUwNzU3ODM2NTg3MTkzNDQtNTEyMTg3MjQ5NTczMTAwOA)**

🌱 **[REACTION MECHANISM ✘ ACID SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTExNDgyMTMyMDAzMzQwNjQwLTExNTI1MjE1MDQ2NjM0MTUy)**

🌱 **[REACTION MECHANISM ✘ ACID SIR HINDI 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTExODQxODI1MzE4Mjc5NDk2LTExODc4ODk2Nzc0MTM2NzA0)**
  
🌱 **[REACTION MECHANISM ✘ SD SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNzM5NDgzMDg1NjcyNzkyLTEzNzY2NTM1MjI5MTM2MTYw)**
        
        
        ''',
                
        f'''  🔮 **CLASS 12 UNACADEMY UNACADEMY**

    
🌱 **[SOLUTION ✘ TNM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTU3MTEwMDgwNjQ0ODg4MC01ODgxMzM2Mzc1MTg0MDg)**

🌱 **[SOLUTION ✘ TNM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNDQ0OTg3OTI0Mzg4NjY0LTEyNDgxMDU3NDQ5MDA2NDg4)**

🌱 **[SOLUTION ✘ AKM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMDIyMTAwMzE4MjczODQ4LTEzMDMyMTE5NjMwNjY3Njg4)**


🌱 **[ELECTROCHEMISTRY ✘ TNM SIR 2024](https://t.me/{BOT_USERNM}?start=Z2V0LTEwNjkwNjA2MzI0MjI3MjgtMTA4NzA5NTM5NDczMTY0MA)**

🌱 **[ELECTROCHEMISTRY ✘ TNM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNTMwMTUyMDc5NzM2MzA0LTEyNTU3MjA0MjIzMTk5Njcy)**


🌱 **[CHEMCAL KINETICS ✘ TNM SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTEyODM0NzM5MTc2NTA5MDQtMTMwMjUxMDYxMTE5OTIwMA)**

🌱**[CHEMICAL KINETICS ✘ TNM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNDgyMDU5MzgwMjQ1ODcyLTEyNTE1MTIzMTExMTQ1NTQ0)**

🌱 **[CHEMICAL KINETICS ✘ AKM SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTE4MjU1MTg3MTgxNTc2NDgtMTg0MDU0NzY4Njc0ODQwOA)**

🌱 **[CHEMICAL KINETICS ✘ AKM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyOTk3MDUyMDM3Mjg5MjQ4LTEzMDIxMDk4Mzg3MDM0NDY0)**

🌱 **[CHEMICAL KINETICS 19 ✘ SM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzODEzNjI1OTk3Mzg3MjA4LTEzODQzNjgzOTM0NTY4NzI4)**

🌱 **[CHEMICAL KINETICS ✘ LY SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMTgyNDA5MzE2NTc1Mjg4LTEzMjIwNDgyNzAzNjcxODgw)**
''',
          f'''


🌱 **[HYDROCARBONS ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTY3MDI5MTk5OTE0Nzg5Ni02OTAzMzA2MjM5MzU1NzY)**  

🌱 **[HYDROCARBON ✘ YSY SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNzAxNDgyMzIxNjcwOTY4LTEyNzQwNTU3NjQwMDA2OTQ0)**

🌱 **[HYDROCARBON ✘ PK SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNDM2ODk5ODUxMzc4ODI0LTEzNDUwOTI2ODg4NzMwMjAw)**


           
🌱 **[HALOALKANES ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTg0MzYyNjEwMzU2MTMyOC04NTE2NDE1NTM0NzY0MDA)**

🌱 **[HALOALKANE & HALOARENE ✘ PK SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNDUxOTI4ODE5OTY5NTg0LTEzNDU3OTQwNDA3NDA1ODg4)**

🌱 **[ALKYL HALIDE ✘ YSY SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEyNzQxNTU5NTcxMjQ2MzI4LTEyNzQyNTYxNTAyNDg1NzEy)**


🌱 **[ALCHOL PHENOL & ETHER  ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTg1MzY0NTQxNTk1NTE2OC04NTk2NTcwMDMzOTE0NzI)**

🌱 **[ALCOHOL PHENOL & ETHER ✘ PK SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzNDU4OTQyMzM4NjQ1MjcyLTEzNDYxOTQ4MTMyMzYzNDI0)**


🌱 **[ALDEHYDES KETONES ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTg2MTY2MDg2NTg3MDI0MC04NjY2NzA1MjIwNjcxNjA)**


🌱 **[CARBOXYLIC ACID ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTExMDcxMzQwMTk1MTkzMjAtMTEwODEzNTk1MDc1ODcwNA)**


🌱 **[ AMINES ✘ YSY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTEzMjg1NjA4MjM0MjMxODQtMTMzMjU2ODU0ODM4MDcyMA)**

       
        


        
        ''',
              
        
    ]
    
    # Send each piece of information as a separate message
    for info in chemu_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.5)

        await query.answer("UNACADEMY CHEMISTRY LECTURES SENT SUCESSFULLY✅", show_alert=True)
    
        parse_mode=ParseMode.MARKDOWN,
