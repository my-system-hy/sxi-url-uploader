from pyrogram import Client
from database.access import SEXI_MOD
from pyrogram.types import Message
from config import Config

LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""


async def AddUser(bot: Client, update: Message):
    if not await SEXI_MOD.is_user_exist(update.from_user.id):
           await SEXI_MOD.add_user(update.from_user.id)
           await bot.send_message(Config.SEXI_MOD_LOG_CHANNEL, LOG_TEXT_P.format(update.from_user.id, update.from_user.mention))
