from logging import basicConfig, getLogger, INFO, DEBUG, WARNING
from core.err import NerdeBuBilgiAmk
from pyrogram import Client
from os import environ
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
LOGS = getLogger("pyrogram").setLevel(WARNING)

WORKTIME = time()

PREFIXES = ['.','!']

API_ID = os.environ.get("API_ID", None)

API_HASH = os.environ.get("API_HASH", None)

STRING = os.environ.get("STRING", None)

if STRING and API_ID and API_HASH:
    bot = Client(STRING, api_id=API_ID, api_hash=API_HASH)
else:
    raise NerdeBuBilgiAmk('Hesabınız ile ilgili tüm bilgilerini girin!')
    
