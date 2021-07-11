from . import *
from pyrogram import idle

try:
    bot.start()
    print('Athena çalışıyor. Sorununuz varsa t.me/athenasupport a gelin.')
    idle()
except Exception as e:
    print('Bir hata oluştu: {}'.format(str(e)))


