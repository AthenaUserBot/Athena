from core.muin import muinrobot
from athena import BOT_NAME


@muinrobot(pattern='^.alive$')
async def alive(message):
    await message.edit_text(f"""
❤️** < bu sana 🥺
{BOT_NAME} Senin için Çalışıyor!**
""")
