#AthenaUserBot | All plugini

from athena import bot as app
from core.muin import muinrobot
from asyncio import sleep

@muinrobot(outgoing=True, pattern="^.all(?: |$)(.*)")
async def alll(q):
    try:
        sebep = message.command[1]
    except IndexError:
        sebep = ''        
    chat = q.chat.id
    a_=0
    await q.delete()
    async for member in app.iter_chat_members(chat):
        if a_ == 5000:
            break
        a_+=1
        await app.send_message(chat, "[{}](tg://user?id={}) {}".format(member.user.first_name, member.user.id, sebep))
        await sleep(3)


@muinrobot(outgoing=True, pattern="^.alladmin(?: |$)(.*)")
async def _(q):
    try:
        sebep = message.command[1]
    except IndexError:
        sebep = ''        
    chat = q.chat.id
    a_=0
    await q.delete()
    admin_list = [i.user for i in await bot.get_chat_members(call.message.chat.id, filter="administrators")]
    for i in admin_list:
        if a_ == 5000:
            break
        a_+=1
        await app.send_message(chat, "[{}](tg://user?id={}) {}".format(i.first_name, i.id,sebep))
        await sleep(3)

