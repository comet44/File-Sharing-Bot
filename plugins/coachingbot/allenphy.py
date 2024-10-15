
 
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=532)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    alnphy_info = [] 
    if data == "aln_phy":
      alnphy_info = [
        f'''  🔮 **CLASS 11 PHYSICS ALLEN CLASSROOM LECTURES**
        
**🌱 [UNIT AND DIMENSION ✘ SKJ SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTM4NzY0NzE5NjUxNzY2OTYtMzg3OTQ3Nzc1ODg5NDg0OA)**

**🌱 [UNIT AND DIMENSION ✘ VJ SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTM4ODA0Nzk2OTAxMzQyMzItMzg4MzQ4NTQ4Mzg1MjM4NA)**

**🌱 [BASIC MATH ✘ MKP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM4ODQ0ODc0MTUwOTE3NjgtMzg4NzQ5MzIwODgwOTkyMA)**

**🌱 [VECTOR ✘ MKP SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTM4ODg0OTUxNDAwNDkzMDQtMzg5MTUwMDkzMzc2NzQ1Ng)**

**🌱 [KINEMATICS ✘ PMP SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTM4OTI1MDI4NjUwMDY4NDAtMzkxMDUzNzYyNzMxNTc1Mg)**

**🌱 [KINEMATICS ✘ KALPIT AGARWAL SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQyMTUxMjQ3MjQwODg0ODgtNDIyOTE1MTc2MTQzOTg2NA)**

**🌱 [KINEMATICS ✘  MKP SIR   ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5MTE1Mzk1NTg1NTUxMzYtMzkxNzU1MTE0NTk5MTQ0MA)**

**🌱 [KINEMATICS ✘ SV SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5MTg1NTMwNzcyMzA4MjQtMzkyODU3MjM4OTYyNDY2NA)**

**🌱 [NLM ✘  ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5Mjk1NzQzMjA4NjQwNDgtMzk0MTU5NzQ5NTczNjY1Ng)**

**🌱 [NLM ✘ PMP SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5NDI1OTk0MjY5NzYwNDAtMzk1NDYyMjYwMTg0ODY0OA)**

**🌱 [WPE  ✘ ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5NTU2MjQ1MzMwODgwMzItMzk2MzYzOTk4MzAwMzEwNA)**

**🌱 [WPE  ✘ PMP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5NjQ2NDE5MTQyNDI0ODgtMzk3MTY1NTQzMjkxODE3Ng)**

**🌱 [COM ✘ ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5NzI2NTczNjQxNTc1NjAtMzk4MDY3MjgxNDA3MjYzMg)**

**🌱 [COM ✘ PMP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5ODE2NzQ3NDUzMTIwMTYtMzk5MDY5MjEyNjQ2NjQ3Mg)**

**🌱 [CIRCULAR MOTION ✘ ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5OTE2OTQwNTc3MDU4NTYtMzk5NjcwMzcxMzkwMjc3Ng)**

**🌱 [CIRCULAR MOTION ✘ PMP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwMDg3MjY4ODg3NzUzODQtNDAxNTc0MDQwNzQ1MTA3Mg)**

**🌱 [ROTATIONAL ✘  ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTM5OTc3MDU2NDUxNDIxNjAtNDAwNzcyNDk1NzUzNjAwMA)**

**🌱 [ROTATIONAL ✘  PMP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwMTY3NDIzMzg2OTA0NTYtNDAyNjc2MTY1MTA4NDI5Ng)**

**🌱 [GRAVITATION ✘ PMP SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwMjc3NjM1ODIzMjM2ODAtNDAzNDc3NzEwMDk5OTM2OA)**

**🌱 [GRAVITATION ✘ CG SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwMzU3NzkwMzIyMzg3NTItNDA0NjgwMDI3NTg3MTk3Ng)**

**🌱 [FLUID MECHANICS ✘  MG SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTQwNDc4MDIyMDcxMTEzNjAtNDA2ODg0Mjc2MzEzODQyNA)**

**🌱 [FLUID MECHANICS ✘ PK SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ1MjQ3MjE0NzcwNTgxNDQtNDUzNjc0NDY1MTkzMDc1Mg)**

**🌱 [FLUID MECHANICS ✘  KBC SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ1Mzc3NDY1ODMxNzAxMzYtNDU0ODc2NzgyNjgwMzM2MA)**

**🌱 [FLUID MECHANICS ✘ KUMAR GAURAV SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTU4NzAzMTUxMzE1NTA4NTYtNTg4NTM0NDEwMDE0MTYxNg)**

**🌱 [THERMAL PHYSICS ✘  HY SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ1NDk3Njk3NTgwNDI3NDQtNDU2ODgwNjQ1MTU5MTA0MA)**
                                  
**🌱 [THERMAL PHYSICS ✘  RJ SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ1OTI4NTI4MDEzMzYyNTYtNDYwNjg3OTgzODY4NzYzMg)**

**🌱 [SHM ✘  SNG SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ2MDc4ODE3Njk5MjcwMTYtNDYxODkwMzAxMzU2MDI0MA)**

**🌱 [SHM ✘ AC SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU0NDM0OTI0MjM1NzMyNzItNTQ1MzUxMTczNTk2NzExMg)**

**🌱 [WAVE THEORY  NEW  ✘ SNG SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ2MzA5MjYxODg0MzI4NDgtNDY0MTk0NzQzMjA2NjA3Mg)**

**🌱[WAVE MOTION ✘ AC SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU0NTQ1MTM2NjcyMDY0OTYtNTQ2ODU0MDcwNDU1Nzg3Mg)**


    ''',
          
f''' 🔮 **CLASS 11 PHYSICS ALLEN CLASSROOM LECTURES**

🌱**[BASIC MATHS ASP SIR HINDI 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NjQ4MjM0NzE5Nzk0MDgwLTE0NjU2MjUwMTY5NzA5MTUy)**  

🌱**[KINEMATICS ASP SIR HINDI MEDIUM](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NjcyMjgxMDY5NTM5Mjk2LTE0NjkzMzIxNjI1NTY2MzYw)**

**🌱 [NLM 24 ✘ ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ2NTk5ODIxOTQzNzQ5ODQtNDY4MzAyNjYxMjg4MDgxNg)**

🌱**[NLM ASP SIR HINDI MEDIUM](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NjU3MjUyMTAwOTQ4NTM2LTE0NjcxMjc5MTM4Mjk5OTEy)**

**🌱 [WPE 24 ✘ ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ3MDEwNjEzNzUxODk3MjgtNDcxNDA4NjQ4MTMwMTcyMA)**

🌱**[WPE ASP SIR HINDI MEDIUM](https://t.me/{BOT_USERNM}?start=Z2V0LTE0Njk0MzIzNTU2ODA1NzQ0LTE0Njk4MzMxMjgxNzYzMjgw)**

**🌱 [COM  24 ✘ ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ3MTUwODg0MTI1NDExMDQtNDcyNzExMTU4NzQxMzcxMg)**

**🌱 [CIRCULAR MOTION NEW  ✘ ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ2ODQwMjg1NDQxMjAyMDAtNDY4OTAzODIwMDMxNzEyMA)**

**🌱 [ROTATION  NEW ✘ ASP SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ2OTAwNDAxMzE1NTY1MDQtNDcwMDA1OTQ0Mzk1MDM0NA)**

**🌱 [THERMAL PHYSICS NEW  ✘ HY SIR  ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ1Njk4MDgzODI4MzA0MjQtNDU5MTg1MDg3MDA5Njg3Mg)**

🌱**[THERMAL PHYSICS RJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NjA0MTQ5NzQ1MjYxMTg0LTE0NjI1MTkwMzAxMjg4MjQ4)**

**🌱 [SHM NEW  ✘ SNG SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ2MTk5MDQ5NDQ3OTk2MjQtNDYyOTkyNDI1NzE5MzQ2NA)**

**🌱 [ SHM ✘ ANKIT CHATURVEDI ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ0OTc2NjkzMzM1OTQ3NzYtNDUwNzY4ODY0NTk4ODYxNg)**

🌱 **[SHM SM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzOTkyOTcxNjg5MjM2OTQ0LTEzOTk4OTgzMjc2NjczMjQ4)**

🌱**[OSCILLATION RJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NjI2MTkyMjMyNTI3NjMyLTE0NjQ2MjMwODU3MzE1MzEy)**

**🌱 [WAVE THEORY  NEW  ✘ SNG SIR NEW ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ2NDI5NDkzNjMzMDU0NTYtNDY1ODk4MDI2MzEzNTYwMA)**

**🌱 [WAVE MOTION ✘ ANKIT CHATURVEDI ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ1MDg2OTA1NzcyMjgwMDAtNDUyMjcxNzYxNDU3OTM3Ng)**

🌱 **[WAVE THEORY SM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzOTk5OTg1MjA3OTEyNjMyLTE0MDE0MDEyMjQ1MjY0MDA4)**

🌱**[WAVE MOTION SNG SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NjQ3MjMyNzg4NTU0Njk2LTE0NjQ3MjMyNzg4NTU0Njk2)**

''',         
        f'''  🔮 **CLASS 12 PHYSICS ALLEN CLASSROOM LECTURES**

**🌱 [ELECTROSTATICS  ✘ JS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQyMzAxNTM2OTI2NzkyNDgtNDI2MTIxMzU2MTEwMDE1Mg)**

**🌱 [ELECTROSTATICS ✘ RKJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU0Njk1NDI2MzU3OTcyNTYtNTQ5NTU5Mjg0ODAyMTI0MA)**

**🌱 [ELECTROSTATICS ✘ SS SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU1Nzg3NTMxNDA4OTAxMTItNTYwMjc5OTQ5MDYzNTMyOA)**

**🌱 [ELECTROSTATIC ✘ DJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTUxMzU4OTk1MzMwODIzODQtNTE1MTkzMDQzMjkxMjUyOA)**

🌱 **[ELECTROSTATICS RJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzODg3NzY4OTA5MTAxNjI0LTEzOTE5ODMwNzA4NzYxOTEy)**

**🌱[ELECTROSTATICS AKS SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE1MjA2MzEwNDIwMTMwOTY4LTE1MjMxMzU4NzAxMTE1NTY4)**

**🌱[ELECTROSTATICS SD SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE1MzE4NTI2NzE4OTQxOTc2LTE1MzU0NTk2MjQzNTU5ODAw)**

🌱 **[CURRENT ELECTRICITY RJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzOTIwODMyNjQwMDAxMjk2LTEzOTUzODk2MzcwOTAwOTY4)**

**🌱 [CURRENT ELECTRICITY  ✘ JS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ0NDA1NTkyNTI5NDk4ODgtNDQ2MjYwMTc0MDIxNjMzNg)**

**🌱 [CURRENT ELECTRICITY ✘ RKJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU0OTY1OTQ3NzkyNjA2MjQtNTUxNjYzMzQwNDA0ODMwNA)**

**🌱 [CURRENT ELECTRICITY ✘ SS SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU2MDM4MDE0MjE4NzQ3MTItNTYyMDgzNDI1Mjk0NDI0MA)**

**🌱[ CURRENT ELECTRICITY ✘ DJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTUxNTI5MzIzNjQxNTE5MTItNTE2NTk1NzQ3MDI2MzkwNA)**

**🌱[CURRENT ELECTRICITY AKS SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE1MjMyMzYwNjMyMzU0OTUyLTE1MjQ4MzkxNTMyMTg1MDk2)**

**🌱 [CAPACITOR  ✘ JS SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTQ0NjQ2MDU2MDI2OTUxMDQtNDQ3NzYzMDcwODgwNzA5Ng)** 

**🌱 [CAPACITOR ✘ SS SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU2MjE4MzYxODQxODM2MjQtNTYyODg0OTcwMjg1OTMxMg)**

**🌱 [CAPACITOR ✘ RKJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU1MTc2MzUzMzUyODc2ODgtNTUyODY1NjU3ODkyMDkxMg)**

**🌱 [CAPACITOR ✘ DJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTUxNjY5NTk0MDE1MDMyODgtNTE3Mjk3MDk4ODkzOTU5Mg)**

**🌱[CAPACITOR AKS SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE1MjQ5MzkzNDYzNDI0NDgwLTE1MjU2NDA2OTgyMTAwMTY4)**

**🌱 [MAGNETISM ✘ DJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTUxNzM5NzI5MjAxNzg5NzYtNTE5MTAwNTc1MTI0ODUwNA)**

**🌱 [MAGNETISM ✘ RKJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU1Mjk2NTg1MTAxNjAyOTYtNTU1MjcwMjkyODY2NjEyOA)**

**🌱 [EMI ✘ RKJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU1NTM3MDQ4NTk5MDU1MTItNTU2NzczMTg5NzI1Njg4OA)**

**🌱 [EMI ✘ DJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTUxOTIwMDc2ODI0ODc4ODgtNTIwMzAyODkyNjEyMTExMg)**

**🌱 [AC ✘ RKJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTU1Njg3MzM4Mjg0OTYyNzItNTU3Nzc1MTIwOTY1MDcyOA)**

**🌱 [AC ✘ DJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTUyMDQwMzA4NTczNjA0OTYtNTIxMTA0NDM3NjAzNjE4NA)**

**🌱 [EMW ✘ DJ SIR](https://t.me/{BOT_USERNM}?start=Z2V0LTUyMTIwNDYzMDcyNzU1NjgtNTIxNTA1MjEwMDk5MzcyMA)**

**🌱[RAY OPTICS ROHIT ✘ JOHARI SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTUzNDUzMDMxNjIxMTM2NDAtNTM2NDMzOTg1NTY2MTkzNg)**

🌱**[RAY OPTICS SM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzOTU0ODk4MzAyMTQwMzUyLTEzOTgwOTQ4NTE0MzY0MzM2)**

🌱**[WAVE OPTICS RJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NTgxMTA1MzI2NzU1MzUyLTE0NTg3MTE2OTE0MTkxNjU2)**

🌱**[WAVE OPTICS ROHIT ✘ JOHARI SIR ](https://t.me/{BOT_USERNM}?start=Z2V0LTUzMzMyNzk5ODcyNDEwMzItNTM0NDMwMTIzMDg3NDI1Ng)**

🌱**[WAVE OPTICS SM SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTEzOTgxOTUwNDQ1NjAzNzIwLTEzOTkxOTY5NzU3OTk3NTYw)**

🌱**[RAY OPTICS RJ SIR 2025](https://t.me/{BOT_USERNM}?start=Z2V0LTE0NTg4MTE4ODQ1NDMxMDQwLTE0NjAzMTQ3ODE0MDIxODAw)**


''',
              
        
    ]
    
    # Send each piece of information as a separate message
    for info in alnphy_info:
        await query.message.reply_text(info, disable_web_page_preview=True,parse_mode=ParseMode.MARKDOWN)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.5)

        await query.answer("ALLEN CLASSROOM  PHYSICS LECTURES SENT SUCESSFULLY✅", show_alert=True),
