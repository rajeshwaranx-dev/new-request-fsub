import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '23361081'))
API_HASH = environ.get('API_HASH', '0605c5395b91ead763072251e20c3417')
BOT_TOKEN = environ.get('BOT_TOKEN', '8759099843:AAERsXi46LuJ_F1gIXBV963RWdOfAJkV67U')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1714147365 5371238852').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/Master_xkid')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002497903505'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002030715343').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Rajeshbot2:Rajeshx2@rajesh2.tlkdbkn.mongodb.net/?appName=Rajesh2")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://Rajeshbot1:Rajeshx1@cluster0.fxpiygb.mongodb.net/?appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rahul")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Rajiiiiiii')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002614244396'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/70d6683aab0aaedc01973-acad0c1612c516f68a.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002876589875').split()]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002030715343'))
URL = environ.get('URL', '')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002614244396'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Tutorial01Ask")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/Tutorial01Ask")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/Tutorial01Ask")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/d677fcc2f773f3140b9ff-f7d343f57c006d71d6.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "af9171ecc18e306689e6bfc77b59df21801f8221")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "Softurl.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "af9171ecc18e306689e6bfc77b59df21801f8221")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "Softurl.in")
SHORTENER_API3 = environ.get("SHORTENER_API3", "af9171ecc18e306689e6bfc77b59df21801f8221")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "Softurl.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "28800"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "64000"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002807137897')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
FSUB_LINK = os.environ.get("FSUB_LINK", "https://t.me/Askmovies4") 
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002844979596'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '7'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = """<b>🎬 <a href="https://t.me/Askmovieslink1">{file_name}</a></b>  

<b>❤️Jᴏɪɴ »  @Askmovies4🥂
🌐Sᴇᴀʀᴄʜ » @Askmovieslink1</b>
"""
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', True)
