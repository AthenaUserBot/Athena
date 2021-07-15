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
    AFKMOD = True
    await message.edit_text(text)

from pyrogram import filters
from athena import bot

@muinrobot()
async def _(_):
    global AFKMOD,bot
    if AFKMOD:
        it = await it('😆 Artık afk değilim!')
        await bot.send_message(_.chat.id,it)
        AFKMOD = False
    await _.continue_propagation()

@bot.on_message(
    filters.create(lambda _, __, ___: bool(AFKMOD))
    & ~filters.me & ~filters.bot & ~filters.edited & (
        filters.mentioned
        | (
            filters.private
            & ~filters.service
        )
    )
)
async def afkkont(
    message
):
    global TOTALMSSSSGS
    if AFKMOD:
        it = await it('😔 Şuanda sahibim afk:/')
        await message.reply_text(it)
        TOTALMSSSSGS = TOTALMSSSSGS + 1

        
