from athena import AFKMOD
from core.muin import muinrobot
from athena.func import it, ct

TOTALMSSSSGS = 0


@muinrobot(pattern='^.afk')
async def afkmodon(message):
    global AFKMOD
    if AFKMOD:
        text = await it("😳 Şuanda zaten a-afk'sın!")
        return await message.edit_text(text)
    text = await ct("🥺 Artık ekrandan çok uzaktayım..")
    await message.edit_text(text)

from athena import bot

@muinrobot()
async def _(_):
    global AFKMOD, bot
    if AFKMOD:
        it = await it('😆 Artık afk değilim!')
        await bot.send_message(_.chat.id,it)
        AFKMOD = False
    await message.continue_propagation()


@muinrobot(
    incoming=True
):
    global TOTALMSSSSGS
    if AFKMOD:
        it = await it('😔 Şuanda sahibim afk:/')
        await message.reply_text(it)
        int(TOTALMSSSSGS) += 1

        
