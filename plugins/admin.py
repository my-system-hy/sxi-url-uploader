from pyrogram import Client as SEXI_MOD
from pyrogram import filters, enums
from config import Config
from database.access import SEXI_MOD
from plugins.buttons import *

@SEXI_MOD.on_message(filters.private & filters.command('total'))
async def sts(c, m):
    if m.from_user.id != Config.SEXI_MOD_OWNER_ID:
        return 
    total_users = await SEXI_MOD.total_users_count()
    await m.reply_text(text=f"Total user(s) {total_users}", quote=True)


@SEXI_MOD.on_message(filters.private & filters.command("search"))
async def serc(bot, update):

      await bot.send_message(chat_id=update.chat.id, text="🔍 TORRENT SEARCH", 
      parse_mode=enums.ParseMode.HTML, reply_markup=Button.BUTTONS01)
