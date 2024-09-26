from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message
from bot import Bot

# Example Group List (Replace these with actual group IDs)
GROUPS = {
    "MP 1 HINDI": -1002175178138,
    "KUNHARI CRASH": -1002007781807,
    "KOTA CQ 1": -1002202198119,

@Bot.on_start()
async def on_start(bot: Bot):
    owner_id = 1828345056  # Owner's Telegram ID
    await bot.send_message(owner_id, "🔄 Bot restarted! Automatically checking admin permissions in groups...")

    async def check_admin_permissions():
        for group_name, group_id in GROUPS.items():
            try:
                # Refresh the Telegram cache by fetching the latest group data
                chat = await bot.get_chat(group_id)

                # Check if the bot is an admin in the group
                member = await bot.get_chat_member(group_id, bot.me.id)

                if member.status != ChatMemberStatus.ADMINISTRATOR:
                    await bot.send_message(owner_id, f"❌ Bot is NOT an admin in {group_name} ({group_id})")
                else:
                    await bot.send_message(owner_id, f"✅ Bot is an admin in {group_name} ({group_id})")

            except PeerIdInvalid:
                # Handle error if bot is not in the group or the group is invalid
                await bot.send_message(owner_id, f"⚠️ Error: Could not access {group_name} ({group_id}). The bot might not be in this group.")
            
            except Exception as e:
                # Handle any other exceptions
                await bot.send_message(owner_id, f"⚠️ Error checking {group_name}: {str(e)}")

    # Call the inner function to check admin permissions
    await check_admin_permissions()

    await bot.send_message(owner_id, "✅ Admin status and cache refresh complete after restart.")
