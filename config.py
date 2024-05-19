import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26184984")
API_HASH = os.environ.get("API_HASH", "d89d7c5ac61ea8f467a6a75aa54a51ca")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "6087816605:AAFsPV-uIOs8OhTSF9PN2lOE2GbdAzMTep8")

CHANNEL = os.environ.get("CHANNEL", "cine_huntsupdates") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","Renamerkbot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","cine_huntsupdates") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","cine_huntsupdates") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","cine_huntsupdates")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","renameone")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://dapita1597:0irZBo8nAyTn9pdu@cluster0.zurtp5f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/file/114c280222bd5826202b1.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6506664860').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002146552264"))
