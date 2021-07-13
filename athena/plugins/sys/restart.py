from athena import BOT_NAME, bot as app
from athena.func import to_be_sent
from core.muin import muinrobot
import os,sys

@muinrobot(pattern='^.restart')
async def restart(event):
    await event.edit_text(f'🔄 {BOT_NAME} yeniden başlatılıyor..')
    try:
        await app.stop()
    except:
        pass
    os.execl(sys.executable, sys.executable, *sys.argv)
