import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=962)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    biualn_info = [] 
    if data == "aln_bio":
      biualn_info = [
        f'''  🔮 **CLASS 11 BIOLOGY ALLEN CLASSROOM LECTURES**

**🌱[ PLANT DIVERSITY ✘ IA SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMwMzI4NDU4NjE2MTUzNjgtMzA0NTg3MDk2NzcyNzM2MA)**

**🌱[ PLANT DIVERSITY ✘ SKJ SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMwNDc4NzQ4MzAyMDYxMjgtMzA2NDkwNzY2MTI3NTY1Ng)**

**🌱[ PLANT DIVERSITY ✘ RM SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMwNjU5MDk1OTI1MTUwNDAtMzA4NDk0NjI4NjA2MzMzNg)**

**🌱[ PLANT DIVERSITY ✘ JS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMwODU5NDgyMTczMDI3MjAtMzA5Nzk3MTM5MjE3NTMyOA)**

**🌱[ ANIMAL DIVERSITY ✘ RS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMwOTg5NzMzMjM0MTQ3MTItMzEwOTk5NDU2NzA0NzkzNg)**

**🌱[ ANIMAL DIVERSITY ✘ AO SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxMTA5OTY0OTgyODczMjAtMzEyMzAxOTY3MzE1OTkyOA)**

**🌱[ MORPHOLOGY ✘ RSK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxMjQwMjE2MDQzOTkzMTItMzEzMTAzNTEyMzA3NTAwMA)** 

**🌱[ MORPHOLOGY ✘ DA SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxMzIwMzcwNTQzMTQzODQtMzEzOTA1MDU3Mjk5MDA3Mg)**

**🌱[ MORPHOLOGY ✘ SKJ SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxNTUwODE0NzI4MjAyMTYtMzE2MjA5NDk5MTQ5NTkwNA)**

🌱**[MORPHOLOGY DA SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0OTAwNzIxMzkyMTE4ODQ4LTE0OTA2NzMyOTc5NTU1MTUy)**

**🌱[ PLANT ANATOMY ✘ DA SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxNjMwOTY5MjI3MzUyODgtMzE3MjExNDMwMzg4OTc0NA)**

**🌱[ PLANT ANATOMY ✘ RSK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxNzMxMTYyMzUxMjkxMjgtMzE4MDEyOTc1MzgwNDgxNg)** 

**🌱[ PLANT ANATOMY ✘ SKJ SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxNDgwNjc5NTQxNDQ1MjgtMzE1NDA3OTU0MTU4MDgzMg)**

**🌱[ PLANT ANATOMY ✘ NKY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxODExMzE2ODUwNDQyMDAtMzE5MDE0OTA2NjE5ODY1Ng)**

**🌱[ PLANT ANATOMY  DA SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0OTA3NzM0OTEwNzk0NTM2LTE0OTA4NzM2ODQyMDMzOTIw)**

**🌱[ ANIMAL TISSUE  ✘ SM SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxOTExNTA5OTc0MzgwNDAtMzE5NjE2MDY1MzYzNDk2MA)**

**🌱[ ANIMAL TISSUE  ✘ SK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMxOTcxNjI1ODQ4NzQzNDQtMzIwNTE3ODAzNDc4OTQxNg)**

**🌱[ COCKROACH ✘ RS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyMDYxNzk5NjYwMjg4MDAtMzIxMDE4NzY5MDk4NjMzNg)**

**🌱[ COCKROACH ✘ AO SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyMTExODk2MjIyMjU3MjAtMzIxNTE5NzM0NzE4MzI1Ng)**

**🌱[ COCKROACH ✘ SK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyMTYxOTkyNzg0MjI2NDAtMzIyMDIwNzAwMzM4MDE3Ng)**

**🌱[ EARTHWORM ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyMjEyMDg5MzQ2MTk1NjAtMzIyODIyMjQ1MzI5NTI0OA)**

**🌱[ FROG ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyMjkyMjQzODQ1MzQ2MzItMzIzMTIyODI0NzAxMzQwMA)**

**🌱[ CELL BIOLOGY ✘ MKG SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyMzIyMzAxNzgyNTI3ODQtMzI0MTI0NzU1OTQwNzI0MA)** 

**🌱[ CELL BIOLOGY ✘ YB SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyNDIyNDk0OTA2NDY2MjQtMzI1MDI2NDk0MDU2MTY5Ng)** 

**🌱[ CELL BIOLOGY ✘ JS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyNTEyNjY4NzE4MDEwODAtMzI2NzI5Nzc3MTYzMTIyNA)**

**🌱[ CELL BIOLOGY ✘ PG SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyNjgyOTk3MDI4NzA2MDgtMzI4MjMyNjc0MDIyMTk4NA)**

🌱 **[CELL BIOLOGY MP SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0MTM5MjUzNjUwMTg3MDA4LTE0MTUxMjc2ODI1MDU5NjE2)**

**🌱[ BIOMOLECULES ✘ ATR SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyODMzMjg2NzE0NjEzNjgtMzI4NjMzNDQ2NTE3OTUyMA)**

**🌱[ BIOMOLECULES ✘ MKG SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyODczMzYzOTY0MTg5MDQtMzI5MTM0NDEyMTM3NjQ0MA)**

**🌱[ ENZYME ✘ JS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyOTIzNDYwNTI2MTU4MjQtMzI5NTM1MTg0NjMzMzk3Ng)**

**🌱 [NERVOUS SYSTEM ✘ RS SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU4ODYzNDYwMzEzODEwMDAtNTg5MTM1NTY4NzU3NzkyMA)**

**🌱 [DIGESTION ✘ RS SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU5Mjc0MjUyMTIxOTU3NDQtNTkzMDQzMTAwNTkxMzg5Ng)**

**🌱 [EXCRETION ✘ RS SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU5MzE0MzI5MzcxNTMyODAtNTkzMzQzNjc5OTYzMjA0OA)**

**🌱 [MUSCLE ✘ RS SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU5MzQ0Mzg3MzA4NzE0MzItNTkzNDQzODczMDg3MTQzMg)**

**🌱 [NERVOUS SYSTEM MEP BATCH ✘ RS SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU5MzU0NDA2NjIxMTA4MTYtNTkzOTQ0ODM4NzA2ODM1Mg)**

**🌱[ PLANT PHYSIOLOGY ✘ JS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMyOTYzNTM3Nzc1NzMzNjAtMzMwMzM2NzI5NjI0OTA0OA)**

**🌱[ PLANT PHYSIOLOGY ✘ MKG SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMzMDUzNzExNTg3Mjc4MTYtMzMyODQxNTU3NzIzMzY0OA)**

🌱**[PHOTOSYNTHESIS MKG SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0ODc0NjcxMTc5ODk0ODY0LTE0ODgzNjg4NTYxMDQ5MzIw)**

**🌱[BOTANY  LEC  01 - 40 ✘ AREEF NASEER SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU3MzUwNTQ0MTQyMzQwMTYtNTc3NDEyOTczMjU2OTk5Mg)**

**🌱[BOTANY LEC 41 - 63  ✘  AREEF NASEER SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTU3NzUxMzE2NjM4MDkzNzYtNTc5NzE3NDE1MTA3NTgyNA)**

**🌱[ HUMAN PHYSIOLOGY ✘ SM SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMzMjk0MTc1MDg0NzMwMzItMzM3MTQ5ODYyMDUyNzE2MA)**

**🌱[ HUMAN PHYSIOLOGY ✘ SK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMzNzI1MDA1NTE3NjY1NDQtMzM5ODU1MDc2Mzk5MDUyOA)**

🌱**[RESPIRATION MKG SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0ODg0NjkwNDkyMjg4NzA0LTE0ODg5NzAwMTQ4NDg1NjI0)**

**🌱[ HUMAN PHYSIOLOGY ✘ SK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTMzOTk1NTI2OTUyMjk5MTItMzQzMDYxMjU2MzY1MDgxNg)**        
        
        
        ''',
                
        f'''  🔮 **CLASS 12 ALLEN CLASSROOM LECTURES **

**🌱 [SEXUAL REPRODUCTION IN FLOWERING PLANTS ✘ RSK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM0MzE2MTQ0OTQ4OTAyMDAtMzQzODYyODAxMzU2NTg4OA)**

**🌱 [SEXUAL REPRODUCTION IN FLOWERING PLANTS ✘ DA SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM0Mzk2Mjk5NDQ4MDUyNzItMzQ0ODY0NzMyNTk1OTcyOA)**

**🌱 [SEXUAL REPRODUCTION IN FLOWERING PLANTS ✘ NKY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM0NDk2NDkyNTcxOTkxMTItMzQ1NjY2Mjc3NTg3NDgwMA)**

🌱**[SEXUAL REPRODUCTION IN FLOWERING PLANTS DA SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0ODkwNzAyMDc5NzI1MDA4LTE0ODk5NzE5NDYwODc5NDY0)**

**🌱 [HUMAN REPRODUCTION & REPRODUCTIVE HEALTH ✘ PC SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM0NTc2NjQ3MDcxMTQxODQtMzQ2NjY4MjA4ODI2ODY0MA)**

**🌱 [HUMAN REPRODUCTION & REPRODUCTIVE HEALTH ✘ SK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM0Njc2ODQwMTk1MDgwMjQtMzQ3ODcwNTI2MzE0MTI0OA)**
                                                       
**🌱 [HUMAN REPRODUCTION & REPRODUCTIVE HEALTH ✘ AR SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTM0Nzk3MDcxOTQzODA2MzItMzQ5ODc0Mzg4NzkyODkyOA)**

**🌱 [PRINCIPLES OF INHERITANCE AND VARIATION ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM1MDU3NTc0MDY2MDQ2MTYtMzUyNDc5NDEwMDE1MjkxMg)** 

**🌱 [PRINCIPLES OF INHERITANCE AND VARIATION ✘ GA SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM1MjU3OTYwMzEzOTIyOTYtMzUzODgyMTEzNzUwNDI4OA)**

**🌱 [MOLECULAR BASIS OF INHERITANCE ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM1Mzk4MjMwNjg3NDM2NzItMzU1Njg1NTg5OTgxMzIwMA)**

**🌱 [MOLECULAR BASIS OF INHERITANCE ✘ GA SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM1NTc4NTc4MzEwNTI1ODQtMzU3Mzg4ODczMDg4MjcyOA)**

🌱 **[MOLECULAR BASIS OF INHERITANCE ✘ MP SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0MDc4MTM1ODQ0NTg0NTg0LTE0MTAxMTgwMjYzMDkwNDE2)**

🌱**[MOLECULAR BASIS OF INHERITANCE ✘ MKG SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0ODM3NTk5NzI0MDM3NjU2LTE0ODYxNjQ2MDczNzgyODcy)**

**🌱[MOLECULAR BASIS OF INHERITANCE MJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0OTk4OTEwNjUzNTc4NDgwLTE1MDE4OTQ5Mjc4MzY2MTYw)**

**🌱[GENETICS MJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE1MDE5OTUxMjA5NjA1NTQ0LTE1MDI5OTcwNTIxOTk5Mzg0)**

**🌱 [EVOLUTION ✘ SK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM1NzQ4OTA2NjIxMjIxMTItMzU4MzkwODA0MzI3NjU2OA)**

**🌱 [EVOLUTION ✘ AR SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM1ODQ5MDk5NzQ1MTU5NTItMzU5NDkyOTI4NjkwOTc5Mg)**

**🌱 [EVOLUTION ✘ MJ STAR](https://t.me/{BOT_USERNM}?start=Z2V0LTE0ODA2NTM5ODU1NjE2NzUyLTE0ODE5NTY0OTYxNzI4NzQ0)**

**🌱 [EVOLUTION ✘ MJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0OTc1ODY2MjM1MDcyNjQ4LTE0OTg3ODg5NDA5OTQ1MjU2)**

**🌱 [HUMAN HEALTH AND DISEASE ✘ MOH SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM1OTU5MzEyMTgxNDkxNzYtMzYxMTk2MjExNzk3OTMyMA)**

**🌱 [HUMAN HEALTH AND DISEASE ✘ PG SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM2MTI5NjQwNDkyMTg3MDQtMzYyODk5NDk0OTA0ODg0OA)**

**🌱 [HUMAN HEALTH & DISEASE ✘ MJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0OTg4ODkxMzQxMTg0NjQwLTE0OTk3OTA4NzIyMzM5MDk2)**
 
**🌱 [STRATEGIES FOR ENHANCEMENT IN FOOD PRODUCTION ✘ SK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM2Mjk5OTY4ODAyODgyMzItMzYzNDAwNDYwNTI0NTc2OA)**

**🌱 [STRATEGIES FOR ENHANCEMENT IN FOOD PRODUCTION ✘ LV SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM2MzUwMDY1MzY0ODUxNTItMzYzNzAxMDM5ODk2MzkyMA)**

**🌱 [MICROBES IN HUMAN WELFARE & PLANT BREEDING ✘ MKG SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM2MzgwMTIzMzAyMDMzMDQtMzY0NDAyMzkxNzYzOTYwOA)**

**🌱 [MICROBES IN HUMAN WELFARE ✘ GA SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM2NDUwMjU4NDg4Nzg5OTItMzY0NzAyOTcxMTM1Nzc2MA)**

🌱**[MICROBES MKG SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0ODcxNjY1Mzg2MTc2NzEyLTE0ODczNjY5MjQ4NjU1NDgw)**

🌱 **[MICROBES IN HUMAN WELFARE MP SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0MTE0MjA1MzY5MjAyNDA4LTE0MTE5MjE1MDI1Mzk5MzI4)**

**🌱 [BIOTECHNOLOGY ✘ MKG SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM2NDgwMzE2NDI1OTcxNDQtMzY1OTA1Mjg4NjIzMDM2OA)**

**🌱 [BIOTECHNOLOGY ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM2NjAwNTQ4MTc0Njk3NTItMzY2ODA3MDI2NzM4NDgyNA)**

**🌱 [BIOTECHNOLOGY ✘ GA SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM2NjkwNzIxOTg2MjQyMDgtMzY3NjA4NTcxNzI5OTg5Ng)**

🌱 **[BIOTECHNOLOGY MP SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0MTAzMTg0MTI1NTY5MTg0LTE0MTEzMjAzNDM3OTYzMDI0)**

🌱**[BIOTECHNOLOGY MKG SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0ODYyNjQ4MDA1MDIyMjU2LTE0ODcwNjYzNDU0OTM3MzI4)**

**🌱 [ECOLOGY ✘ IA SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM2NzcwODc2NDg1MzkyODAtMzcwMzEzNzg2MDc2MzI2NA)**

**🌱 [ECOLOGY ✘ SDS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3MDQxMzk3OTIwMDI2NDgtMzcyMjE3NDU1NDMxMTU2MA)**

**🌱 [ECOLOGY ✘ MC SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3MjMxNzY0ODU1NTA5NDQtMzc1NDIzNjM1Mzk3MTg0OA)**        

🌱**[POI MKG SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0ODIwNTY2ODkyOTY4MTI4LTE0ODM3NTk5NzI0MDM3NjU2)**

    ''',
f''' 🔮 **BIOLOGY  ALLEN CLASSROOM LECTURES**

**🌱 [DIGESTION AND ABSORPTION ✘ PIYUSH CHAUDHARY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxMjQ5NTA5MTI1NDM5MjgtNDEyOTk2MDU2ODc0MDg0OA)**

**🌱 [EXCRETORY ✘ PIYUSH CHAUDHARY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxMzA5NjI0OTk5ODAyMzItNDEzNDk3MDIyNDkzNzc2OA)**

**🌱 [RESPIRATION ✘ PIYUSH CHAUDHARY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxMzU5NzIxNTYxNzcxNTItNDEzODk3Nzk0OTg5NTMwNA)**

**🌱 [BODY FLUID AND CIRCULATION ✘  PIYUSH CHAUDHARY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxMzg5Nzc5NDk4OTUzMDQtNDE0Mjk4NTY3NDg1Mjg0MA)**

**🌱 [CHEMICAL CONTROL AND COORDINATION ✘ PIYUSH CHAUDHARY SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTQxNDM5ODc2MDYwOTIyMjQtNDE0ODk5NzI2MjI4OTE0NA)**

**🌱 [SENSE ORGANS ✘ PIYUSH CHAUDHARY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxNDk5OTkxOTM1Mjg1MjgtNDE1MzAwNDk4NzI0NjY4MA)**

**🌱 [SKELTAL SYSTEM ✘ PIYUSH CHAUDHARY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxNTQwMDY5MTg0ODYwNjQtNDE1NjAxMDc4MDk2NDgzMg)**

**🌱 [LOCOMOTION ✘ PIYUSH CHAUDHARY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxNTcwMTI3MTIyMDQyMTYtNDE1ODAxNDY0MzQ0MzYwMA)**

**🌱 [BIOTECH ✘ ASHUTOSH GAUR SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ0ODA2MzY1MDI1MjUyNDgtNDQ5MDY1NTgxNDkxOTA4OA)**

**🌱 [PLANT BREEDING ✘ ASHUTOSH GAUR SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ0OTE2NTc3NDYxNTg0NzItNDQ5MjY1OTY3NzM5Nzg1Ng)**

**🌱 [BIOMOLECULE ✘ ASHUTOSH GAUR SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ0OTM2NjE2MDg2MzcyNDAtNDQ5NjY2NzQwMjM1NTM5Mg)**

**🌱 [HUMAN HEALTH AND DISEASE ✘ ASHUTOSH GAUR ](https://t.me/{BOT_USERNM}?start=Z2V0LTU4NTcyOTAwMjU0Mzg4NjQtNTg2OTMxMzIwMDMxMTQ3Mg)**

**🌱 [ECOLOGY ✘ PRANVENDRA SINGH SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU4OTIzNTc2MTg4MTczMDQtNTkyNTQyMTM0OTcxNjk3Ng)**

''',


          
    f''' 🔮**ATR SIR ALLEN [LATEST] **

🌱**[PHOTOSYNTHESIS ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwNjk4NDQ2OTQzNzc4MDgtNDA3NDg1NDM1MDU3NDcyOA)**

🌱**[RESPIRATION ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwNzU4NTYyODE4MTQxMTItNDA3Nzg2MDE0NDI5Mjg4MA)**

🌱**[ENZYME ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwNzc4NjAxNDQyOTI4ODAtNDA3ODg2MjA3NTUzMjI2NA)**

🌱**[TRANSPORTATION IN PLANTS ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwNzg4NjIwNzU1MzIyNjQtNDA4Mjg2OTgwMDQ4OTgwMA)**

🌱**[MINERAL ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwODI4Njk4MDA0ODk4MDAtNDA4Mzg3MTczMTcyOTE4NA)**

🌱**[PLANT HORMONE ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwODM4NzE3MzE3MjkxODQtNDA4NTg3NTU5NDIwNzk1Mg)**

🌱**[BIOMOLECULE ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwODU4NzU1OTQyMDc5NTItNDA4NTg3NTU5NDIwNzk1Mg)**

🌱**[PRINCIPLE OF INHERITANCE ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwODY4Nzc1MjU0NDczMzYtNDEwMTkwNjQ5NDAzODA5Ng)**

🌱**[BIOTECHNOLOGY ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxMDE5MDY0OTQwMzgwOTYtNDEwNjkxNjE1MDIzNTAxNg)**

🌱**[PLANT BREEDING ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxMDc5MTgwODE0NzQ0MDAtNDExMDkyMzg3NTE5MjU1Mg)**

🌱**[MOLECULAR BASIS OF INHERITANCE ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxMTE5MjU4MDY0MzE5MzYtNDEyMjk0NzA1MDA2NTE2MA)**

🌱**[MICROBES IN HUMAN WELFARE ](https://t.me/{BOT_USERNM}?start=Z2V0LTQxMjM5NDg5ODEzMDQ1NDQtNDEyMzk0ODk4MTMwNDU0NA)**

    ''',
f'''
🔮 **MP SIR 2024**

🌱 **[BIOTECHNOLOGY  ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3NTUyMzgyODUyMTEyMzItMzc2MDI0Nzk0MTQwODE1Mg)** 

🌱 **[BIOTECHNOLOGY APPLICATION ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3NjEyNDk4NzI2NDc1MzYtMzc2NDI1NTY2NjM2NTY4OA)**

🌱 **[MICROBES ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3NjQyNTU2NjYzNjU2ODgtMzc2NTI1NzU5NzYwNTA3Mg)**

🌱 **[PLANT BREEDING ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3NjYyNTk1Mjg4NDQ0NTYtMzc2NzI2MTQ2MDA4Mzg0MA)**

🌱 **[BIOMOLECULES  ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3NjgyNjMzOTEzMjMyMjQtMzc3MjI3MTExNjI4MDc2MA)**

🌱 **[CELL BIOLOGY ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3NzIyNzExMTYyODA3NjAtMzc4MTI4ODQ5NzQzNTIxNg)**

🌱 **[CELL CYCLE AND DIVISON ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3ODIyOTA0Mjg2NzQ2MDAtMzc4NTI5NjIyMjM5Mjc1Mg)**

🌱 **[PRINCIPLE OF INHERITANCE ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM3ODYyOTgxNTM2MzIxMzYtMzgwNzMzODcwOTY1OTIwMA)**

🌱 **[MOLECULAR BASIS OF INHERITANCE ✘ MP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM4MDgzNDA2NDA4OTg1ODQtMzgyNTM3MzQ3MTk2ODExMg)** 

''',

          
        
    ]
    
    # Send each piece of information as a separate message
    for info in biualn_info:
        await query.message.reply_text(info, disable_web_page_preview=True ,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.1)

        await query.answer("ALLEN CLASSROOM  BIOLOGY LECTURES SENT SUCESSFULLY✅", show_alert=True)
