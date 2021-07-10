from core.muin import muinrobot

@muinrobot(pattern='^.alive$')
async def alive(message):
    await message.edit_text("✨ **Athena Çalışıyor!**")
