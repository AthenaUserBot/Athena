from . import *
from pyrogram import idle
from .plugins.extra.zup import tg_userbotinstaller

try:
    bot.stop()
except:
    print("Athena starting...")
finally:
    bot.start()
    tg_userbotinstaller()

bot.set_parse_mode()

try:
    print('Athena çalışıyor. Sorununuz varsa t.me/athenasupport a gelin.')
    idle()
except Exception as e:
    print('Bir hata oluştu: {}'.format(str(e)))


