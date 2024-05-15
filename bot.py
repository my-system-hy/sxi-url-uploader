import os
import logging
from config import Config
from pyrogram import Client as SEXI_MOD
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.SEXI_MOD_DOWNLOAD_LOCATION):
        os.makedirs(Config.SEXI_MOD_DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    SX = SEXI_MOD(name="@SEXI_MOD",
    bot_token=Config.SEXI_MOD_BOT_TOKEN,
    api_id=Config.SEXI_MOD_API_ID,
    api_hash=Config.SEXI_MOD_API_HASH,
    plugins=plugins)
    SX.run()
