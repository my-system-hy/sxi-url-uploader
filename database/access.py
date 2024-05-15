
from config import Config
from database.database import Database

SEXI_MOD = Database(Config.SEXI_MOD_DATABASE_URL, Config.SEXI_MOD_SESSION_NAME)
