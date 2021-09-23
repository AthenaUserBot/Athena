from athena import BOT_NAME, bot
from athena.func import to_be_sent
from core.muin import athena
from os import execl
import sys

@athena(pattern='^.restart')
async def restart(event):
    await event.edit_text(f'🔄 {BOT_NAME} yeniden başlatılıyor..')
    try:
        await bot.restart()
    except:
        pass
    execl(sys.executable, sys.executable, *sys.argv)
