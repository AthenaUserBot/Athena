from athena import AFKMOD
from core.muin import muinrobot
from athena.func import it, ct

@muinrobot(pattern='^.afk')
async def afkmodon(message):
    global AFKMOD
    if AFMOD:
        text = await it("😳 Şuanda zaten a-afk'sın!")
        return await message.edit_text(text)
    text = await ct("🥺 Artık ekrandan çok uzaktayım..")
    await message.edit_text(text)
