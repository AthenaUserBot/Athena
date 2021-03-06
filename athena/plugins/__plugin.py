from core.muin import athena
from athena import bot

@athena(pattern="^.plist")
async def plist(_):
    await _.edit_text("Kontrol ediliyor...")
    yuklenen = f"💕 **Pluginler**\n\n"
    yuklenens = str(yuklenen)
    async for plugin in bot.search_messages("me", filter="document"):
        try:
            dosyaismi = plugin.document.file_name.split(".")[1]
        except:
            continue

        if dosyaismi == "py":
            yuklenens += f"🌈 {plugin.document.file_name}\n"
    try:
        if yuklenen != yuklenens:
            await _.edit_text(yuklenens)
        else:
            await _.edit_text('🤦🏻‍♂️ Plugin bulunamadı.')
    except:
        await _.reply_text(yuklenens)
