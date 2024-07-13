# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23770935"))
API_HASH = getenv("API_HASH", "b4148cc1194323cc977ebc91bbf9263f")
BOT_TOKEN = getenv("BOT_TOKEN", "7371760847:AAGSdIzWatWqUX8RbP0vPhB7BBHomwkLEtc")
OWNER_ID = int(getenv("OWNER_ID", "1387249506"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://iamanonymus24:SMF9dLKyjE76erfV@cluster0.sb3zs6x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
FORCESUB = getenv("FORCESUB", "BOTADMINCHANNE")
