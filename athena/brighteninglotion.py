from . import *
import importlib
from pyrogram import idle
import chromedriver_autoinstaller
from .plugins import ALL_MODULES as AM
from importlib import import_module as im
from core.help.plugin import tg_userbotinstaller

try:
    bot.start()
    sl(5)
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    tg_userbotinstaller()
    from core.err.ree import raa, rac, ccc
    for car in rac:
       ccc(bot,car)
    from core.err.ree import aaa
    bot.stop()
except Exception as e:
    LOGS.error("Bir hata oluştu...\n>>" + str(e))


for i in AM:
    imported_module = im("athena.plugins." + i)


LOGS.warning('Athena başlatılıyor. Sorununuz varsa t.me/athenasupport a gelin.')

bot.run()
