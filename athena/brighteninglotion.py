from . import *
from pyrogram import idle
import chromedriver_autoinstaller
from core.help.plugin import tg_userbotinstaller

try:
    bot.start()
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    tg_userbotinstaller()
    from core.err.ree import raa, rac, ccc
    for car in rac:
       ccc(bot,car)
    from core.err.ree import aaa
    idle()
except Exception as e:
    LOGS.error("Bir hata oluştu...\n>>" + str(e))


LOGS.warning('Athena başlatılıyor. Sorununuz varsa t.me/athenasupport a gelin.')
