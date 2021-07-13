from athena import AFKMOD
from core.muin import muinrobot
from athena.func import it, ct

@muinrobot(pattern='^.afk')
async def afkmodon(message):
    global AFKMOD
    if AFMOD:
        return await message.edit_text(await it("😳 Şuanda zaten a-afk'sın!"))
    await message.edit_text(await ct("🥺 Artık ekrandan çok uzaktayım.."))
