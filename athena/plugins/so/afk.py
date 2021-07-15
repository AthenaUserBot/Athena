from athena import AFKMOD
from athena.func import it, ct
from core.muin import muinrobot
from core.help import send_botlog

TOTALMSSSSGS = 0
AFK_ALLOWEDUSER = {}

@muinrobot(pattern='^.afk')
async def afkmodon(message):
    global AFKMOD
    if AFKMOD:
        text = await it("😳 Şuanda zaten a-afk'sın!")
        return await message.edit_text(text)
    text = await ct("🥺 Artık ekrandan çok uzaktayım..")
    await send_botlog(
        await ct('#AFK\n') + text
    )    #Botlog'a bildir
    AFKMOD = True
    await message.edit_text(text)

from pyrogram import filters
from athena import bot

@muinrobot()
async def _(_):
    global AFKMOD,bot
    if AFKMOD:
        AFKMOD = False
        await bot.send_message(
            _.chat.id,
            await it('😆 Artık afk değilim!')
            )
        await send_botlog(
            await ct('#NoAFK\nAFK iken gelen mesaj sayısı : {TOTALMSSSSGS}')
        )     #Botlog'a bildir
        TOTALMSSSSGS = 0
    await _.continue_propagation()

@bot.on_message(
    filters.create(lambda _, __, ___: bool(AFKMOD))
    & ~filters.me
    & ~filters.bot
    & ~filters.edited & (
        filters.mentioned
        | (
            filters.private
            & ~filters.service
        )
    )
)
async def afkkont(
    client,
    message
):
    global TOTALMSSSSGS
    if AFKMOD:
        await message.reply_text(
            await it('😔 Şuanda sahibim afk:/'),
            quote=True
        )
        TOTALMSSSSGS = TOTALMSSSSGS + 1
    await message.continue_propagation()
        
