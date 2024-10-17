from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message
from bot import Bot
from config import ADMINS, BOT_USERNM

# Example Group List (Replace these with actual group IDs)
GROUPS = {
    "MP 1 HINDI": -1002175178138, 
    "MP 1 ENGLISH" : -1002181583963,
    "MP 3 ENGLISH": -1002049819461,  # Replace with your actual group IDs
    "KUNHARI CRASH": -1002007781807,  # Replace with your actual group IDs
    "KOTA CQ 1": -1002202198119, 
    "DREAM 2025": -1002159837565,       
}
# Manual command to check admin permissions
@Bot.on_message(filters.command("joiner_start") & filters.user(ADMINS) ,group = 6672)
async def joiner_start_command(bot: Bot, message: Message):
    # Define the function inside the command
    async def check_admin_permissions():
        for group_name, group_id in GROUPS.items():
            try:
                # Check if the bot is an admin in the group
                member = await bot.get_chat_member(group_id, bot.me.id)

                if member.status != ChatMemberStatus.ADMINISTRATOR:
                    await message.reply_text(f"❌ Bot is NOT an admin in {group_name} ({group_id})")
                else:
                    await message.reply_text(f"✅ Bot is an admin in {group_name} ({group_id})")

            except PeerIdInvalid:
                # Handle error if bot is not in the group or the group is invalid
                await message.reply_text(f"⚠️ Error: Could not access {group_name} ({group_id}). The bot might not be in this group.")
            
            except Exception as e:
                # Handle any other exceptions
                await message.reply_text(f"⚠️ Error checking {group_name}: {str(e)}")

    # Call the internal function to perform the check
    await message.reply_text("🔍 Checking admin status in groups...")
    await check_admin_permissions()
    await message.reply_text("✅ Admin status check complete.")
