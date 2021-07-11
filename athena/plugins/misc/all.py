#AthenaUserBot | All plugini

from athena import bot as app, TEMP, BOT_NAME
from athena.func import extract_text
from core.muin import muinrobot
from asyncio import sleep

@muinrobot(outgoing=True, pattern="^.all(?: |$)(.*)")
async def alll(q):
    sebep = await extract_text(q)

    ben = TEMP['ME'].id

    chat = q.chat.id

    a_=0
    seb = f'"{sebep} ' + 'için"' if sebep != '' else ''
    await q.edit_text(f'**🔄 {BOT_NAME} {seb} etiketlemeyi başlatıyor..**')

    async for member in app.iter_chat_members(chat):
        if a_ == 5000:
            break
        if member.user.id == ben:
            continue
        else:
            a_+=1
        await app.send_message(chat, "[{}](tg://user?id={}) {}".format(member.user.first_name, member.user.id, sebep))
        await sleep(3)
    await app.send_message(chat,f"**✅ {BOT_NAME} etiketleme işlemini bitirdi..\n🗒️ Toplam {a_} kişi etiketlendi..**")


@muinrobot(outgoing=True, pattern="^.alladmin(?: |$)(.*)")
async def alladmin(q):
    sebep = await extract_text(q)
    chat = q.chat.id
    a_=0

    ben = TEMP['ME'].id

    seb = f'"{sebep} ' + 'için"' if sebep != '' else ''
    await q.edit_text(f'**🔄 {BOT_NAME} {seb} admin etiketlemesini başlatıyor..**')
    admin_list = [i.user for i in await bot.get_chat_members(chat, filter="administrators")]
    for i in admin_list:
        if a_ == 5000:
            break
        if member.user.id == ben:
            continue
        else:
            a_+=1
        await app.send_message(chat, "[{}](tg://user?id={}) {}".format(i.first_name, i.id,sebep))
        await sleep(3)
    await app.send_message(chat,f"**✅ {BOT_NAME} admin etiketleme işlemini bitirdi..**")

