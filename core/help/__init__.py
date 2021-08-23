async def eor(
    _,
    __
):
    try:
        return await _.edit_text(__)
    except:
        return await _.reply_text(__)

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
