from core.muin import athena
from athena import BOT_NAME


@athena(pattern='^.alive$')
async def alive(message):
    await message.edit_text(f"""
❤️** < bu sana 🥺
{BOT_NAME} Senin için Çalışıyor!**
""")
