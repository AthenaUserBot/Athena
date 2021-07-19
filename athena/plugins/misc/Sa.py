import asyncio

from core.muin import muinrobot

@muinrobot(pattern="^Sa$")
async def merkurkedissa(event):


    animation_interval = 0.4

    animation_ttl = range(0, 12)

    await event.edit_text("Selamün Aleyküm..🐺")

    animation_chars = [
        
            "S",
            "SA",
            "SEA",
            "**Selam Almayanın Mq**",
            "🌀Sea",
            "🍃Selam",
            "🔅Sa",
            "🍁Selammm",
            "🍃Naber",
            "🔅Ben Geldim",
            "**Hoşgeldim**",
            "**❄️Sea**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit_text(animation_chars[i % 12])