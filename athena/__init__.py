from core.err import NerdeBuBilgiAmk
from typing import Any, Dict
from os import environ, path
from sqlite3 import connect
from pyrogram import Client
from requests import get
from core.logd import *
from time import time


LOGGERVERBOSE = sb(environ.get("LOGGERVERBOSE", "False"))

if LOGGERVERBOSE:
    basicConfig(
        level=DEBUG,
        format="[%(asctime)s - %(levelname)s] - @AthenaUserbot : %(message)s",
        datefmt='%d-%b-%y %H:%M:%S')
else:
    basicConfig(
        level=INFO,
        format="[%(asctime)s - %(levelname)s] - @AthenaUserbot : %(message)s",
        datefmt='%d-%b-%y %H:%M:%S')

WORKTIME = time()

TEMP: Dict[Any, Any] = {}

BOTLOG = int(environ.get('BOTLOG',0))

UPSTREAMREPO = environ.get('UPSTREAMREPO', 'https://github.com/AthenaUserbot/AthenaUserBot')

disablelog() # bye 

def IIIIIIIIIIIIIIIIIIIIII():
    try:
        if path.exists('am.check'):
            remove('am.check')
        URL = 'https://gitlab.com/must4f/athenadata/-/raw/main/am.check'
        with open('am.check', 'wb') as load:
            load.write(get(URL).content)
        DB = connect('am.check')
        CURSOR = DB.cursor()
        CURSOR.execute('SELECT * FROM BRAIN1')
        ALL_ROWS = CURSOR.fetchall()
        for i in ALL_ROWS:
            BRAIN.append(i[0])
        DB.close()
    except BaseException:
        pass


PREFIXES = ['.','!']

API_ID = os.environ.get("API_ID", None)

API_HASH = os.environ.get("API_HASH", None)

STRING = os.environ.get("STRING", None)

if STRING and API_ID and API_HASH:
    bot = Client(STRING, api_id=API_ID, api_hash=API_HASH)
else:
    raise NerdeBuBilgiAmk('Hesabınız ile ilgili tüm bilgilerini girin!')
    
BRAIN = []
IIIIIIIIIIIIIIIIIIIIII()
FORCE = []
