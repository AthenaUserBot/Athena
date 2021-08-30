import os
from . import *
import importlib
from pyrogram import idle
import chromedriver_autoinstaller
from importlib import import_module as im
from .plugins import *

try:
    sl(5)
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    from core.err.ree import raa, rac, ccc
    for car in rac:
       ccc(bot,car)
except Exception as e:
    LOGS.error("Bir hata oluştu...\n>>" + str(e))

Yuklenenler = 'Yüklenen Modüller: '
for i in ALL_MODULES:
    imported_module = im("athena.plugins." + i)
    Yuklenenler += str(i) + ','

LOGS.warning('Athena başlatılıyor. Sorununuz varsa t.me/athenasupport a gelin.')

LOGS.info(os.listdir("athena/"))



LOGS.info(Yuklenenler)

idle()
