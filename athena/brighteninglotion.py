import os
from . import *
import importlib
from pyrogram import idle
import chromedriver_autoinstaller
from .plugins import ALL_MODULES as AM
from importlib import import_module as im

try:
    bot.start()
    sl(5)
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    for message in bot.search_messages("me", filter="document"):
        file_name = message.document.file_name

        try:
            pymi = file_name.split('.')[-1]
        except:
            continue

        if pymi == 'py':
            if not os.path.exists("./athena/plugins/" + file_name):
                plugin = bot.download_media(message,f"./athena/plugins/")
                LOGS.info(f'{file_name} yüklendi!')
            else:
                LOGS.warning(f'{file_name} atlandı!')
#                pass # Şimdilik
    from core.err.ree import raa, rac, ccc
    for car in rac:
       ccc(bot,car)
except Exception as e:
    LOGS.error("Bir hata oluştu...\n>>" + str(e))

Yuklenenler = 'Yüklenen Modüller: '
for i in AM:
    imported_module = im("athena.plugins." + i)
    Yuklenenler += str(i) + ','

LOGS.warning('Athena başlatılıyor. Sorununuz varsa t.me/athenasupport a gelin.')

LOGS.info(Yuklenenler)

idle()
