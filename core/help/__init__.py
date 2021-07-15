async def ReplyOrE(message,text):
    try:
        return await message.edit_text(text)
    except:
        return await message.reply_text(text)

from athena import BOTLOG, bot

async def send_botlog(
    _
):
    if BOTLOG:
        try:
            return await bot.send_message(
            BOTLOG,
            _
            )
        except:
            return None
    else:
        return None

    
