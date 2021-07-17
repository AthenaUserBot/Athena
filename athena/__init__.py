from logging import CRITICAL, WARNING, ERROR, DEBUG, INFO, basicConfig, getLogger
from core.err import NerdeBuBilgiAmk
from distutils.util import strtobool
from typing import Any, Dict
from os import environ, path
from sqlite3 import connect
from pyrogram import Client
from requests import get
from time import time

LOGGERVERBOSE = strtobool(environ.get("LOGGERVERBOSE", "False"))

WORKTIME = time()

def disablelogs(): #thx to teamderuntergang
    pyrogram_main = getLogger('pyrogram')
    pyrogram_main.setLevel(WARNING)
    pyrogram_syncer = getLogger('pyrogram.syncer')
    pyrogram_syncer.setLevel(CRITICAL)
    pyrogram_syncer = getLogger('pyrogram.client')
    pyrogram_syncer.setLevel(ERROR)
    pyrogram_session = getLogger('pyrogram.session.session')
    pyrogram_session.setLevel(CRITICAL)
    pyrogram_auth = getLogger('pyrogram.session.auth')
    pyrogram_auth.setLevel(CRITICAL)

ATHENAVER = 'v0.1'

TEMP: Dict[Any, Any] = {}

try:
    BOTLOG = int(environ.get('BOTLOG',0))
except:
    BOTLOG = 0

UPSTREAMREPO = environ.get('UPSTREAMREPO', 'https://github.com/AthenaUserbot/AthenaUserBot')

disablelogs() # bye 

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

BOT_NAME = environ.get("BOT_NAME", 'athena')
BOT_NAME = BOT_NAME.title()

API_ID = environ.get("API_ID", None)

API_HASH = environ.get("API_HASH", None)

STRING = environ.get("STRING", None)

plugins= dict(
    root="athena.plugins",
    exclude=["test"]            
)

if API_ID and API_HASH:
    bot = Client(STRING if STRING else ':memory:',
        api_id=API_ID,
        api_hash=API_HASH,
        device_model='@muinrobot',
        system_version=' | Sorularınız için @AthenaSupport',
        app_version=str('| ' + ATHENAVER),
        hide_password=True,
        sleep_threshold=180,
        plugins=plugins
)
else:
    acont = '✅' if API_ID is not None else '❌'
    hcont = '✅' if API_HASH is not None else '❌'
    raise NerdeBuBilgiAmk(f'Hesabınız ile ilgili tüm bilgilerini girin!\n>>>>  API_ID {acont}\n>>>>  API_HASH: {hcont}')
   


BRAIN = []
IIIIIIIIIIIIIIIIIIIIII()
FORCE = []
AFKMOD = False

