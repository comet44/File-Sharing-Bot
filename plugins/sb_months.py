import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from pyrogram.enums import ParseMode
from bot import Bot
from helper_func import subscribed, encode, decode, get_messages


@Bot.on_callback_query(group=436)
async def hlpcallback(client: Bot, query: CallbackQuery):
    data = query.data
    
    if data == "mp_1":
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» `Master Pro 1`

🌀 **Full Name »»** `Abhinav Batch for NEET 2024`
⚜️ **Start At:** 14 Jun, 2023""",
            reply_markup=InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton("Jun 2023", callback_data="junmp1"),
            InlineKeyboardButton("Jul 2023", callback_data="julmp1"),
        ],
        [
            InlineKeyboardButton("Aug 2023", callback_data="augmp1"),
            InlineKeyboardButton("Sept 2023", callback_data="septmp1"),
        ],
        [
            InlineKeyboardButton("Oct 2023", callback_data="octmp1"),
            InlineKeyboardButton("Nov 2023", callback_data="novmp1"),
        ],
        [
            InlineKeyboardButton("Dec 2023", callback_data="decmp1"),
            InlineKeyboardButton("Jan 2024", callback_data="janmp1"),
        ],
        [
            InlineKeyboardButton("Feb 2024", callback_data="febmp1"),
            InlineKeyboardButton("MArch 2024", callback_data="marmp1"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],    
        ],
        ),
   parse_mode=ParseMode.MARKDOWN,         
        )
    elif data == "sb_start_1":
        # Handle crx case
        
        await query.message.edit_text(
            text = """CHOOSE THE BATCH:


🌱 Page  1/3""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("Master Pro 1", callback_data="mp_1"),
            InlineKeyboardButton("Master Pro 2", callback_data="mp_2"),
        ],
        [
            InlineKeyboardButton("Growth", callback_data="growth"),
            InlineKeyboardButton("Elite", callback_data="elite"),
        ],
        [
            InlineKeyboardButton("Dream", callback_data="dream"),
            InlineKeyboardButton("CB 2", callback_data="cb2"),
        ],
        [
            InlineKeyboardButton("Early Excel", callback_data="earlyexcel"),
            InlineKeyboardButton("CC 3", callback_data="cc3"),
        ],
        [
            InlineKeyboardButton("CB 4", callback_data="cb4"),
            InlineKeyboardButton("CE 4", callback_data="ce4"),
        ],
        [
            InlineKeyboardButton("Conquer 1", callback_data="cq1"),
            InlineKeyboardButton("Conquer 2", callback_data="cq2"),
        ],
        [
            InlineKeyboardButton("✗", callback_data="close"),
            InlineKeyboardButton("⇒⇒", callback_data="sb_start_2"),
        ],
        
        ]
    ),
    parse_mode=ParseMode.MARKDOWN,        
    )    
    elif data == "sb_start_2":
        # Handle crx case
        
        await query.message.edit_text(
            text = """CHOOSE THE BATCH:


🌱 Page  2/3""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("Conquer 11", callback_data="cq11"),
            InlineKeyboardButton("Conquer 13", callback_data="cq13"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("✗", callback_data="close"),
        ],
        
        ]
    ),
    parse_mode=ParseMode.MARKDOWN,        
    )
    elif data == "mp_2":
        # Handle crx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Master Pro 2

🌀 **Full Name »»** `Prashiksha Batch NEET UG 2024`
⚜️ **Start At:**3 July, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("Jul 2023", callback_data="julmp2"),
            InlineKeyboardButton("Aug 2023", callback_data="augmp2"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septmp2"),
            InlineKeyboardButton("Oct 2023", callback_data="octmp2"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novmp2"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],            
    ],       
            ),
    parse_mode=ParseMode.MARKDOWN,     
        )

    elif data == "growth":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Growth Batch

🌀 **Full Name »»** `Akshar Batch for NEET 2025`
⚜️ **Start At:** 9 June, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("Jun 2023", callback_data="jungrowth"),
            InlineKeyboardButton("Jul 2023", callback_data="julgrowth"),
        ],
        [
            InlineKeyboardButton("Aug 2023", callback_data="auggrowth"),
            InlineKeyboardButton("Sept 2023", callback_data="septgrowth"),
        ],
        [
            InlineKeyboardButton("Oct 2023", callback_data="octgrowth"),
            InlineKeyboardButton("Nov 2023", callback_data="novgrowth"),
        ],
        [
            InlineKeyboardButton("Dec 2024", callback_data="octgrowth"),
        ],            
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],            
                ],
            ),
    parse_mode=ParseMode.MARKDOWN,     
        )
   
    elif data == "elite":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Elite Batch

🌀 **Full Name »»** `Umang Batch NEET UG 2024 (Physics & Chemistry)`
⚜️ **Start At:** 15 July, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("Jul 2023", callback_data="julelite"),
            InlineKeyboardButton("Aug 2023", callback_data="augelite"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septelite"),
            InlineKeyboardButton("Oct 2023", callback_data="octelite"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novelite"),
            InlineKeyboardButton("Dec 2023", callback_data="decelite"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN,
        )
    elif data == "dream":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Dream Batch

🌀 **Full Name »»** `Dream Batch for NEET UG 2024`
⚜️ **Start At:** 7 June, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("Jul 2023", callback_data="jundream"),
            InlineKeyboardButton("Jul 2023", callback_data="juldream"),
        ],    
        [    
            InlineKeyboardButton("Aug 2023", callback_data="augdream"),
            InlineKeyboardButton("Sept 2023", callback_data="septdream"),
        ],
        [    
            InlineKeyboardButton("Oct 2023", callback_data="octdream"),
            InlineKeyboardButton("Nov 2023", callback_data="novdream"),
        ],
        [
            InlineKeyboardButton("Dec 2023", callback_data="decdream"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
      ),
parse_mode=ParseMode.MARKDOWN,
        )
    elif data == "cb2":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» CB-2

🌀 **Full Name »»** `Kota NEET UG 2024 CB-2`
⚜️ **Start At:** 15 May, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("May 2023", callback_data="maycb2"),
            InlineKeyboardButton("Jun 2023", callback_data="juncb2"),
        ],
        [
            InlineKeyboardButton("Jul 2023", callback_data="julcb2"),
            InlineKeyboardButton("Aug 2023", callback_data="augcb2"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septcb2"),
            InlineKeyboardButton("Oct 2023", callback_data="octcb2"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novcb2"),
            InlineKeyboardButton("Dec 2023", callback_data="deccb2"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN,
        )
    elif data == "cc3":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» CC-3

🌀 **Full Name »»** `Kota NEET UG 2024 CC-3`
⚜️ **Start At:** 30 May, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("May 2023", callback_data="maycc3"),
            InlineKeyboardButton("Jun 2023", callback_data="juncc3"),
        ],
        [
            InlineKeyboardButton("Jul 2023", callback_data="julcc3"),
            InlineKeyboardButton("Aug 2023", callback_data="augcc3"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septcc3"),
            InlineKeyboardButton("Oct 2023", callback_data="octcc3"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novcc3"),
            InlineKeyboardButton("Dec 2023", callback_data="deccc3"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN,
        )
    elif data == "cb4":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» CB-4

🌀 **Full Name »»** `Kota NEET UG 2024 CB-4`
⚜️ **Start At:** 14 June, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("Jul 2023", callback_data="julcb4"),
            InlineKeyboardButton("Aug 2023", callback_data="augcb4"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septcb4"),
            InlineKeyboardButton("Oct 2023", callback_data="octcb4"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novcb4"),
            InlineKeyboardButton("Dec 2023", callback_data="deccb4"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN,
        )
    elif data == "ce4":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »»  CE-4

🌀 **Full Name »»** `Kota NEET UG 2024 CE-4`
⚜️ **Start At:** 18 July, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("Jul 2023", callback_data="julce4"),
            InlineKeyboardButton("Aug 2023", callback_data="augce4"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septce4"),
            InlineKeyboardButton("Oct 2023", callback_data="octce4"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novce4"),
            InlineKeyboardButton("Dec 2023", callback_data="decce4"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN
        )
    elif data == "earlyexcel":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Early Excel 1

🌀 **Full Name »»** `Kota NEET 2024 Early Excel 1`
⚜️ **Start At:** 27 January, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("Jan 2023", callback_data="janearlyexcel"),
            InlineKeyboardButton("Feb 2023", callback_data="febearlyexcel"),
        ],
        [
            InlineKeyboardButton("Mar 2023", callback_data="marearlyexcel"),
            InlineKeyboardButton("Apr 2023", callback_data="aprearlyexcel"),
        ],
        [
            InlineKeyboardButton("May 2023", callback_data="mayearlyexcel"),
            InlineKeyboardButton("Jun 2023", callback_data="junearlyexcel"),
        ],
        [
            InlineKeyboardButton("Jul 2023", callback_data="julearlyexcel"),
            InlineKeyboardButton("Aug 2023", callback_data="augearlyexcel"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septearlyexcel"),
            InlineKeyboardButton("Oct 2023", callback_data="octearlyexcel"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novearlyexcel"),
            InlineKeyboardButton("Dec 2023", callback_data="decearlyexcel"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN
        )
    elif data == "cq1":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Conquer-01

🌀 **Full Name »»** `Sanyam Batch`
⚜️ **Start At:** 15 April, 2023""",
            reply_markup=InlineKeyboardMarkup(
        
        [
        [
            InlineKeyboardButton("Mar 2023", callback_data="marcq1"),
            InlineKeyboardButton("Apr 2023", callback_data="aprcq1"),
        ],
        [
            InlineKeyboardButton("May 2023", callback_data="maycq1"),
            InlineKeyboardButton("Jun 2023", callback_data="juncq1"),
        ],
        [
            InlineKeyboardButton("Jul 2023", callback_data="julcq1"),
            InlineKeyboardButton("Aug 2023", callback_data="augcq1"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septcq1"),
            InlineKeyboardButton("Oct 2023", callback_data="octcq1"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novcq1"),
            InlineKeyboardButton("dec 2023", callback_data="deccq1"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN
        )
    elif data == "cq2":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Conquer 02

🌀 **Full Name »»** `Yash Batch for NEET UG 2024`
⚜️ **Start At:** 15 April, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("Mar 2023", callback_data="marcq2"),
            InlineKeyboardButton("Apr 2023", callback_data="aprcq2"),
        ],
        [
            InlineKeyboardButton("May 2023", callback_data="maycq2"),
            InlineKeyboardButton("Jun 2023", callback_data="juncq2"),
        ],
        [
            InlineKeyboardButton("Jul 2023", callback_data="julcq2"),
            InlineKeyboardButton("Aug 2023", callback_data="augcq2"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septcq2"),
            InlineKeyboardButton("Oct 2023", callback_data="octcq2"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novcq2"),
            InlineKeyboardButton("dec 2023", callback_data="deccq2"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN
        )
    elif data == "cq4":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Conquer 04

🌀 **Full Name »»** `Prerna Batch NEET UG 2024`
⚜️ **Start At:** 30 May, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
        [
            InlineKeyboardButton("May 2023", callback_data="maycq4"),
            InlineKeyboardButton("Jun 2023", callback_data="juncq4"),
        ],
        [
            InlineKeyboardButton("Jul 2023", callback_data="julcq4"),
            InlineKeyboardButton("Aug 2023", callback_data="augcq4"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septcq4"),
            InlineKeyboardButton("Oct 2023", callback_data="octcq4"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novcq4"),
            InlineKeyboardButton("Dec 2023", callback_data="deccq4"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN
        )
    elif data == "cq8":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Conquer 08

🌀 **Full Name »»** `Kartavya Batch for NEET 2024`
⚜️ **Start At:**28 June, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [                   
        [
            InlineKeyboardButton("May 2023", callback_data="maycq8"),
            InlineKeyboardButton("Jun 2023", callback_data="juncq8"),
        ],
        [
            InlineKeyboardButton("Jul 2023", callback_data="julcq8"),
            InlineKeyboardButton("Aug 2023", callback_data="augcq8"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septcq8"),
            InlineKeyboardButton("Oct 2023", callback_data="octcq8"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novcq8"),
            InlineKeyboardButton("Dec 2023", callback_data="deccq8"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN
        )
    elif data == "cq11":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Conquer 11

🌀 **Full Name »»** `Sanshodhan Batch NEET UG 2024`
⚜️ **Start At:** 03, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("Jul 2023", callback_data="julcq11"),
            InlineKeyboardButton("Aug 2023", callback_data="augcq11"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septcq11"),
            InlineKeyboardButton("Oct 2023", callback_data="octcq11"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novcq11"),
            InlineKeyboardButton("Dec 2023", callback_data="deccq11"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN
        )
    elif data == "cq13":
        # Handle btx case
        
        await query.message.edit_text(
            text = """**☘️BATCH NAME** »» Conquer 13

🌀 **Full Name »»** `Pahal Batch for NEET UG 2024`
⚜️ **Start At:** 31 July, 2023""",
            reply_markup=InlineKeyboardMarkup(
                [
                           
        [
            InlineKeyboardButton("Jul 2023", callback_data="julcq13"),
            InlineKeyboardButton("Aug 2023", callback_data="augcq13"),
        ],
        [
            InlineKeyboardButton("Sept 2023", callback_data="septcq13"),
            InlineKeyboardButton("Oct 2023", callback_data="octcq13"),
        ],
        [
            InlineKeyboardButton("Nov 2023", callback_data="novcq13"),
            InlineKeyboardButton("Dec 2023", callback_data="deccq13"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="sb_start_1"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
        ],
        ),
    parse_mode=ParseMode.MARKDOWN,
        )
