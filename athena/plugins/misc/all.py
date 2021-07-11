#AthenaUserBot | All plugini

from athena.func import extract_text
from athena import bot as app
from core.muin import muinrobot
from asyncio import sleep

@muinrobot(outgoing=True, pattern="^.all(?: |$)(.*)")
async def alll(q):
    sebep = await extract_text(q)

    chat = q.chat.id

    a_=0
    seb = f'"{sebep}' + 'için"' if sebep else ''
    await q.edit_text(f'**🔄 Athena {seb} etiketlemeyi başlatıyor..**')

    async for member in app.iter_chat_members(chat):
        if a_ == 5000:
            break
        a_+=1
        await app.send_message(chat, "[{}](tg://user?id={}) {}".format(member.user.first_name, member.user.id, sebep))
        await sleep(3)


@muinrobot(outgoing=True, pattern="^.alladmin(?: |$)(.*)")
async def alladmin(q):
    sebep = await extract_text(q)
    chat = q.chat.id
    a_=0
    await q.delete()
    admin_list = [i.user for i in await bot.get_chat_members(chat, filter="administrators")]
    for i in admin_list:
        if a_ == 5000:
            break
        a_+=1
        await app.send_message(chat, "[{}](tg://user?id={}) {}".format(i.first_name, i.id,sebep))
        await sleep(3)

