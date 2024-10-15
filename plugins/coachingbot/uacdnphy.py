import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages
from pyrogram import __version__
from config import OWNER_ID, BOT_USERNM


@Bot.on_callback_query(group=637)
async def bot_nots(client: Bot, query: CallbackQuery):
    data = query.data
    coach_info = [] 
    if data == "un_phy":
      coach_info = [
        f'''  🔮 <b>CLASS 11 PHYSICS UNACADEMY</b>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyNjMxMzQ3MTM0OTE0MDg4LTEyNjM1MzU0ODU5ODcxNjI0"><b>UNIT &amp; DIMENDION ✘ SHARAD MATHUR 2025</b></a>


🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExMjk4Nzc4NTg2NTMzMzY4LTExMzI4ODM2NTIzNzE0ODg4"><b>BASIC MATHS ✘ PARVEZ KHAN SIR 2025</b></a>
        
🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExNjg5NTMxNzY5ODkzMTI4LTExNzIwNTkxNjM4MzE0MDMy"><b>BASIC MATHS ✘ PARVEZ KHAN SIR HINDI MEDIUM </b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEyNDIzOTQ3MzY4MzYxNi0xNDEyNzIzMDQ3NTMxNDQ"><b>VECTORS AND BASIC MATHS ✘ AG SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE0MDU3MDk1Mjg4NTU3NTItMTQxMjcyMzA0NzUzMTQ0MA"><b> BASIC MATHS ✘ YN SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMjUxNjE1MTk1MTg3NTUyLTEyMjcyNjU1NzUxMjE0NjE2"><b>BASIC MATH ✘ SIKANDER SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzMTM4MzI0MzQyMDQyMzkyLTEzMTU4MzYyOTY2ODMwMDcy"><b>BASIC MATHS ✘ AG SIR DREAM 2025</b></a>


🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE0MTM3MjQ5Nzg3NzA4MjQtMTQyMTc0MDQyODY4NTg5Ng"><b> VECTOR ✘ YN SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE3MDcyOTA4MzE5MTAzMzYtMTcyMjMxOTgwMDUwMTA5Ng"><b> VECTOR ✘ PARVEZ SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMDYyMjUwMTkwOTQzOTc2LTEyMDc2Mjc3MjI4Mjk1MzUy"><b>VECTOR ✘ ST SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyODc4ODI0MTUxMDQxOTM2LTEyODk3ODYwODQ0NTkwMjMy"><b>VECTOR ✘ ANURAG GARG 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNDYyOTUwMDYzNjAyODA4LTEzNDczOTcxMzA3MjM2MDMy"><b>VECTOR ✘ YN SIR 2025</b></a>




🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExMzI5ODM4NDU0OTU0MjcyLTExMzQ3ODczMjE3MjYzMTg0"><b>KINEMATICS ✘ PARVEZ KHAN SIR 2025 </b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExNzIxNTkzNTY5NTUzNDE2LTExNzM2NjIyNTM4MTQ0MTc2"><b>KINEMATICS ✘ PK HINDI MEDIUM</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTE0MjI3NDIzNTk5MjUyOC0xNTkzMDcwNjcwNjIwNTY"><b>NLM ✘ AG SIR </b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEzMzM1NzA0Nzk2MjAxMDQtMTM0NzU5NzUxNjk3MTQ4MA"><b>NLM ✘ ANURAG GARG SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE0MjI3NDIzNTk5MjUyODAtMTQ0MDc3NzEyMjIzNDE5Mg"><b> NLM ✘ YN SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExMzQ4ODc1MTQ4NTAyNTY4LTExMzYwODk4MzIzMzc1MTc2"><b>NLM ✘ PARVEZ KHAN SIR 2025</b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEzNDg1OTk0NDgyMTA4NjQtMTM1MTYwNTI0MTkyOTAxNg"<b>FRICTION ✘ ANURAG GARG SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExNzM3NjI0NDY5MzgzNTYwLTExNzQ5NjQ3NjQ0MjU2MTY4"><b>NLM ✘ PK HINDI MERIUM</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMDc1Mjc1Mjk3MDU1OTY4LTEyMTA4MzM5MDI3OTU1NjQw"><b>NLM ✘ ST SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMjczNjU3NjgyNDU0MDAwLTEyMjgwNjcxMjAxMTI5Njg4"><b>NLM ✘ SIKANDER SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyODk4ODYyNzc1ODI5NjE2LTEyOTI2OTE2ODUwNTMyMzY4"><b>NLM ✘ ANURAG GARG SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNDc0OTczMjM4NDc1NDE2LTEzNDkyMDA2MDY5NTQ0OTQ0"><b>NLM ✘ YN SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNjE2MjQ1NTQzMjI4NTYwLTEzNjMzMjc4Mzc0Mjk4MDg4"><b>NLM*✘ YN SIR 2025</b></a>



🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTY1NjI2NDk2MTc5NjUyMC02NjkyOTAwNjc5MDg1MTI"><b>WPE ✘ AG SIR </b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEzNTI2MDcxNzMxNjg0MDAtMTM2MzYyODQxNjgwMTYyNA"><b>WPE ✘ ANURAG GARG SIR</b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTE0NDI3ODA5ODQ3MTI5NjAtMTQ1MzgwMjIyODM0NjE4NA"><b>WPE ✘ YN SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExMzYxOTAwMjU0NjE0NTYwLTExMzcyOTIxNDk4MjQ3Nzg0"><b>WPE ✘ PARVEZ KHAN SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExNzQ5NjQ3NjQ0MjU2MTY4LTExNzYxNjcwODE5MTI4Nzc2"><b>WPE ✘ PK HINDI MEDIUM</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMTA5MzQwOTU5MTk1MDI0LTEyMTE4MzU4MzQwMzQ5NDgw"><b>WPE ✘ ST SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMjgwNjcxMjAxMTI5Njg4LTEyMjk3NzA0MDMyMTk5MjE2"><b>WPE ✘ SIKANDER SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyOTI3OTE4NzgxNzcxNzUyLTEyOTM3OTM4MDk0MTY1NTky"><b>WPE ✘ ANURAG GARG SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNDkyMDA2MDY5NTQ0OTQ0LTEzNTAzMDI3MzEzMTc4MTY4"><b>WPE ✘ YN SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNjM0MjgwMzA1NTM3NDcyLTEzNjQ3MzA1NDExNjQ5NDY0"><b>WPE* ✘ YN SIR 2025</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTg4NDcwNTI4NDM3NjA3Mi04OTU3MjY1MjgwMDkyOTY"><b>COM ✘ AG SIR </b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEzNjQ2MzAzNDgwNDEwMDgtMTM3NDY0OTY2MDQzNDg0OA"<b>COLLISION AND COM ✘ ANURAG GARG SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMjk4NzA1OTYzNDM4NjAwLTEyMzA1NzE5NDgyMTE0Mjg4"><b>COM ✘ SIKANDER SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyOTM4OTQwMDI1NDA0OTc2LTEyOTUwOTYzMjAwMjc3NTg0"><b>COM ✘ ANURAG GARG SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNTA0MDI5MjQ0NDE3NTUyLTEzNTEzMDQ2NjI1NTcyMDA4"><b>COM ✘ YN SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNjQ4MzA3MzQyODg4ODQ4LTEzNjU4MzI2NjU1MjgyNjg4"><b>COM* ✘ YN SIR 2025</b></a>
''',
          f'''


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTM4MjczNzczMzQ0NDY4ODAtMzg0MzQwODIzNDI3NzAyNA"<b>FLUIDS ✘ ANURAG GARG SIR</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEyMTgzNDgzODcwOTA5NDQtMTIyNzM2NTc2ODI0NTQwMA"><b>CIRCULAR MOTION ✘ AG SIR</b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEzNzU2NTE1OTE2NzQyMzItMTM4NDY2ODk3MjgyODY4OA"><b>CIRCULAR MOTION ✘ ANURAG GARG SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyOTUxOTY1MTMxNTE2OTY4LTEyOTYwOTgyNTEyNjcxNDI0"><b>CIRCULAR MOTION ✘ ANURAG GARG SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNTE0MDQ4NTU2ODExMzkyLTEzNTIxMDYyMDc1NDg3MDgw"><b>CIRCULAR MOTION ✘ YN SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNjU5MzI4NTg2NTIyMDcyLTEzNjY0MzM4MjQyNzE4OTky"><b>CIRCULAR MOTION ✘ YN SIR 2025</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEzODU2NzA5MDQwNjgwNzItMTQwMDY5OTg3MjY1ODgzMg"><b>ROTATIONAL MOTION ✘ ANURAG GARG SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyOTYxOTg0NDQzOTEwODA4LTEyOTcyMDAzNzU2MzA0NjQ4"><b>ROTATIONAL MOTION ✘ ANURAG GARG SIR </b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTk1Njg0NDMzMzYxMTcyMC05ODI4OTQ1NDU4MzU3MDQ"><b>THERMAL PHYSICS ✘ ST SIR</b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTMwMDU3OTM3MTgxNTIwMDAtMzAzMTg0MzkzMDM3NTk4NA"><b>THERMAL PHYSICS MP2 ✘ ST SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzMTE2MjgxODU0Nzc1OTQ0LTEzMTM3MzIyNDEwODAzMDA4"><b>THERMAL PHYSICS ✘ RANJEET BANTHIYA SIR 2025</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTczOTQyNTI1NDY2NTM5MjAtNzQyMDMwMjc1ODg3NzkwNA"><b>SHM AND WAVES MP 1 ✘ SIKANDER SIR </b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTc4MDkwNTIwNzk3NTg4OTYtNzgzNTEwMjI5MTk4Mjg4MA"><b>SHM AND WAVES MP 2 ✘ SIKANDER SIR </b></a>



        
        
        
        ''',
                
        f'''  🔮 <b>CLASS 12 PHYSICS UNACADEMY</b> 

    
🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTMzNjY0ODg5NjQzMzAyNC0zNTc2ODk0NTI0NjAwODg"><b>ELECTROSTATICS ✘ AG SIR 2024</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE1ODUwNTUyMjA3MDU0ODgtMTYxMDEwMzUwMTY5MDA4OA"><b> ELECTROSTATS 2024 </b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExMjE0NjE2MzYyNDI1MTEyLTExMjQwNjY2NTc0NjQ5MDk2">ELECTROSTATICS ✘ BRY 2025 </a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExNjE1Mzg4ODU4MTc4NzEyLTExNjQzNDQyOTMyODgxNDY0"><b>ELECTROSTATICS ✘ BRY HINDI 2025</b></a>

       
🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEwODgwOTczMjU5NzEwMjQtMTEwNDEyODIyNTgwMTE2OA"><b>CURRENT ELECTRICITY ✘ ST SIR 2024</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE2MTExMDU0MzI5Mjk0NzItMTYyODEzODI2Mzk5OTAwMA"><b>CURRENT ELECTRICITY ✘ BRY SIR 2024</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExMjQxNjY4NTA1ODg4NDgwLTExMjU5NzAzMjY4MTk3Mzky"><b>CURRENT ELECTRICITY & CAPACITOR ✘ BRY 2025 </b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExNjQzNDQyOTMyODgxNDY0LTExNjYyNDc5NjI2NDI5NzYw"><b>CURRENT &amp; CAPACITOR ✘ BRY HINDI 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMTkwNDk3Mzg5NTg1MTI4LTEyMTk1NTA3MDQ1NzgyMDQ4"><b>CURRENT ELECTRICITY LEC 1-3 ✘ AG SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNTgyMTc5ODgxMDg5NTA0LTEzNjA1MjI0Mjk5NTk1MzM2"><b>CURRENT & CAPACITOR ✘ ANURAG SUKHIJA SIR 2025</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEzMTc1Mzk1Nzk3ODk5NjAtMTMyNzU1ODg5MjE4MzgwMA"><b>CAPACITOR ✘ ST SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE2MjkxNDAxOTUyMzgzODQtMTYzNzE1NTY0NTE1MzQ1Ng"><b>CAPACITOR ✘ BRY SIR</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTkzNjgwNTcwODgyNDA0MC05NTU4NDI0MDIzNzIzMzY"><b>MEC ✘ AG SIR 2024</b></a>

🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTcxNjI4MDY0MzAzNTYyMTYtNzE4Mzg0Njk4NjM4MzI4MA"><b>MEC ✘ ST SIR 2024 </b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE3MjMzMjE3MzE3NDA0ODAtMTc2NTQwMjg0Mzc5NDYwOA"><b> MEC ✘ PARVEZ SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE2MzkxNTk1MDc2MzIyMjQtMTY1ODE9NjIwMTE4MDUyMA"><b>MEC ✘ BRY SIR 2024</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExMjYwNzA1MTk5NDM2Nzc2LTExMjY5NzIyNTgwNTkxMjMy"><b>MEC ✘ BRY 2025 </b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTExNjYzNDgxNTU3NjY5MTQ0LTExNjcyNDk4OTM4ODIzNjAw"><b>MEC ✘ BRY HINDI 2025</b></a>



🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTEyMjkzNjk2MzA3MjQxNjgtMTI0MDM5MDg3NDM1NzM5Mg"><b>EMI ✘ AG SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE2NjAyMDAwNjM2NTkyODgtMTY3MDIxOTM3NjA5MzEyOA"><b>EMI ✘ BRY SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMDMxMTkwMzIyNTIzMDcyLTEyMDU3MjQwNTM0NzQ3MDU2"><b>EMI ✘ ST SIR 2025</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTIwNjU5ODIyMTU2MDk4MDgtMjA3Mjk5NTczNDI4NTQ5Ng"><b>ALTERNATING CURRENT ✘ AG SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTE2NzEyMjEzMDcyOTI1MTItMTY3NzIzMjg5NDcyODgxNg"><b>ALTERNATING CURRENT ✘ BRY SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMDU4MjQyNDY1OTg2NDQwLTEyMDYxMjQ4MjU5NzA0NTky"><b>ALTERNATING CURRENT ✘ ST SIR 2025</b></a>


''',


f'''      
🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTQzNTg0MDA4OTEzMjA0MC00NjI4OTIyMzI1OTU0MDg"><b>RAY OPTICS ✘ ST SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMTE5MzYwMjcxNTg4ODY0LTEyMTY2NDUxMDM5ODM5OTEy"><b>RAY OPTICS ✘ AG SIR 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyODUxNzcyMDA3NTc4NTY4LTEyODc3ODIyMjE5ODAyNTUy"><b>RAY OPTICS ✘ ST SIR 2025</b></a>



🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMTY3NDUyOTcxMDc5Mjk2LTEyMTc0NDY2NDg5NzU0OTg0"><b>OPTICAL INSTRUMENTS ✘ AG SIR 2025</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTQ4MDkyNjk5NDkwNDMyMC00OTE5NDgyMzg1Mzc1NDQ"><b>WAVE OPTICS ✘ ST SIR</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEyMTc1NDY4NDIwOTk0MzY4LTEyMTg5NDk1NDU4MzQ1NzQ0"><b>WAVE OPTICS ✘ AG SIR 2025</b></a>


🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTczNjgyMDIzMzQ0Mjk5MzYtNzM5MzI1MDYxNTQxNDUzNg"><b>COMPLETE OPTICS✘ AG SIR</b></a>


🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzMTU5MzY0ODk4MDY5NDU2LTEzMTgxNDA3Mzg1MzM1OTA0"><b>MODERN PHYSICS ✘ AG SIR DREAM 2025</b></a>

🌱<a href="https://t.me/{BOT_USERNM}?start=Z2V0LTEzNTU4MTMzNTMxMzQ0Mjg4LTEzNTgxMTc3OTQ5ODUwMTIw"><b>MODERN PHYSICS ✘ ANURAG SUKHIJA SIR 2025</b></a>



🌱<a href= "https://t.me/{BOT_USERNM}?start=Z2V0LTk1ODg0ODE5NjA5MDQ4ODAtOTU5NDQ5MzU0ODM0MTE4NA"><b>SEMI CONDUCTOR ✘ AG SIR</b></a>

        ''',
              
        
    ]
    
    # Send each piece of information as a separate message
    for info in coach_info:
        await query.message.reply_text(info, disable_web_page_preview=True)
        
        # Add a short delay between messages (optional)
        await asyncio.sleep(0.5)

        await query.answer("UNACADEMY PHYSICS LECTURES SENT SUCESSFULLY✅", show_alert=True)
    
        parse_mode=ParseMode.HTML,
   
