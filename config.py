import os
import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # Bot Information 
    SEXI_MOD_BOT_TOKEN = os.environ.get("SEXI_MOD_BOT_TOKEN", "")
    SEXI_MOD_BOT_USERNAME = os.environ.get("SEXI_MOD_BOT_USERNAME", "") # Bot username without @.
    
    # The Telegram API things
    SEXI_MOD_API_ID = int(os.environ.get("SEXI_MOD_API_ID", ""))
    SEXI_MOD_API_HASH = os.environ.get("SEXI_MOD_API_HASH", "")
    
    # the download location, where the HTTP Server runs
    SEXI_MOD_DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Telegram maximum file upload size
    SEXI_MOD_MAX_FILE_SIZE = 50000000
    SEXI_MOD_TG_MAX_FILE_SIZE = 4194304000 #2097152000
    SEXI_MOD_FREE_USER_MAX_FILE_SIZE = 50000000
    
    # chunk size that should be used with requests
    SEXI_MOD_CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    SEXI_MOD_HTTP_PROXY = ""
    
    # maximum message length in Telegram
    SEXI_MOD_MAX_MESSAGE_LENGTH = 4096
    
    # set timeout for subprocess
    SEXI_MOD_PROCESS_MAX_TIMEOUT = 3600
    
    # your telegram account id
    SEXI_MOD_OWNER_ID = int(os.environ.get("SEXI_MOD_OWNER_ID", "")) 
    SEXI_MOD_SESSION_NAME = "UPLOADER-BOT"
    
    # database uri (mongodb)
    SEXI_MOD_DATABASE_URL = os.environ.get("SEXI_MOD_DATABASE_URL", "")
    SEXI_MOD_MAX_RESULTS = "50"

    # channel information
    SEXI_MOD_LOG_CHANNEL = int(os.environ.get("SEXI_MOD_LOG_CHANNEL", "")) # your log channel id and make bot admin in log channel with full right 
    
    # if you want force subscribe then give your channel id below else leave blank
    SEXI_MOD_update_channel = environ.get('SEXI_MOD_UPDATES_CHANNEL', '') # your update channel id and make bot admin in update channel with full right
    SEXI_MOD_UPDATES_CHANNEL = int(SEXI_MOD_update_channel) if SEXI_MOD_update_channel and id_pattern.search(SEXI_MOD_update_channel) else None  
    
    # Url Shortner Information 
    SEXI_MOD = bool(environ.get('SEXI_MOD', True)) # Set False If you want shortlink off else True
    SEXI_MOD_URL = environ.get('SEXI_MOD_URL', 'moneykamalo.com') # your shortlink url domain or url without https://
    SEXI_MOD_API = environ.get('SEXI_MOD_API', '0eefb93e1e3ce9470a7033115ceb1bad13a9d674') # your url shortner api
    SEXI_MOD_TUTORIAL = os.environ.get("SEXI_MOD_TUTORIAL", "https://t.me/How_To_Open_Linkl")


