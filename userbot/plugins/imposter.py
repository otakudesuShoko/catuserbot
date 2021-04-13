"""
Created by @Jisan7509
Credit @Infinity20998
Userbot plugin fot CatUserbot
"""


import asyncio

from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@bot.on(admin_cmd(pattern="imp(|n) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="imp(|n) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    USERNAME = f"tg://user?id={hmm}"
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    text1 = await edit_or_reply(event, "Uhmm... Something is wrong here!!")
    await asyncio.sleep(2)
    await text1.delete()
    stcr1 = await event.client.send_file(
        event.chat_id, "CAADAQADRwADnjOcH98isYD5RJTwAg"
    )
    text2 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** I have to call discussion"
    )
    await asyncio.sleep(3)
    await stcr1.delete()
    await text2.delete()
    stcr2 = await event.client.send_file(
        event.chat_id, "CAADAQADRgADnjOcH9odHIXtfgmvAg"
    )
    text3 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** We have to eject the imposter or will lose "
    )
    await asyncio.sleep(3)
    await stcr2.delete()
    await text3.delete()
    stcr3 = await event.client.send_file(
        event.chat_id, "CAADAQADOwADnjOcH77v3Ap51R7gAg"
    )
    text4 = await event.reply(f"**Others :** Where??? ")
    await asyncio.sleep(2)
    await text4.edit(f"**Others :** Who?? ")
    await asyncio.sleep(2)
    await text4.edit(
        f"**[{DEFAULTUSER}]({USERNAME}) :** Its {name} , I saw {name}  using vent,"
    )
    await asyncio.sleep(3)
    await text4.edit(f"**Others :**Okay.. Vote {name} ")
    await asyncio.sleep(2)
    await stcr3.delete()
    await text4.delete()
    stcr4 = await event.client.send_file(
        event.chat_id, "CAADAQADLwADnjOcH-wxu-ehy6NRAg"
    )
    catevent = await event.reply(f"{name} is ejected.......")
    await asyncio.sleep(2)
    await catevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    await stcr4.delete()
    if cmd == "":
        await catevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} was an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await catevent.delete()
        await event.client.send_file(event.chat_id, "CAADAQADLQADnjOcH39IqwyR6Q_0Ag")
    elif cmd == "n":
        await catevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} was not an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await catevent.delete()
        await event.client.send_file(event.chat_id, "CAADAQADQAADnjOcH-WOkB8DEctJAg")


@bot.on(admin_cmd(pattern="sis(|n) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="sis(|n) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    USERNAME = f"tg://user?id={hmm}"
    event.pattern_match.group(2)
    event.pattern_match.group(1).lower()
    text1 = await edit_or_reply(event, "Anjir group nih sepi bat Goyang dlu ah")
    await asyncio.sleep(2)
    await text1.delete()
    text2 = await edit_or_reply(event, "**Tarik sis...**")
    await asyncio.sleep(2)
    await text2.delete()
    text3 = await edit_or_reply(event, "**Semongkoo 🕺💃...**")
    await asyncio.sleep(2)
    await text3.delete()
    stcr1 = await event.client.send_file(
        event.chat_id,
        "CAACAgQAAx0CVs_uIgADw2B1rgkFThELm-z4lOYbQVXlzYCwAAIHEAACpvFxHrHslPu2V1XQHgQ",
    )
    text4 = await event.reply(f"Kini tinggal aku sendiri..")
    await asyncio.sleep(3)
    await stcr1.delete()
    await text4.delete()
    stcr2 = await event.client.send_file(
        event.chat_id,
        "CAACAgIAAx0CVs_uIgADwmB1r56g8LjaYN8RGiMKqCNyGJcHAAKjAQACEBptIkfOxfML2NdjHgQ",
    )
    text5 = await event.reply(f"Hanya berteman dengan sepi.. ")
    await asyncio.sleep(3)
    await stcr2.delete()
    await text5.delete()
    stcr3 = await event.client.send_file(
        event.chat_id,
        "CAACAgIAAx0CVs_uIgAD7mB1sLNyuat4uDVwhQ8cdmzwO8-eAAIiAwACbbBCA7zHw9-hcLV4HgQ",
    )
    text6 = await event.reply(f"Menanti dirimu kembali. ")
    await asyncio.sleep(3)
    await stcr3.delete()
    await text6.delete()
    stcr4 = await event.client.send_file(
        event.chat_id,
        "CAACAgUAAx0CVs_uIgAD-2B1svW7CXnmLh0X7hDAi-pIzsaBAAIQAQACsdHYVBUD2rnCXthBHgQ",
    )
    text7 = await event.reply(f"Gini bat dah hidup gua udah **jomblo**")
    await asyncio.sleep(2)
    await text7.edit(f"Group chat wa dan tele **sepi**")
    await asyncio.sleep(2)
    await text7.edit(f"Gada duit lagi, Anjing beban keluarga")


@bot.on(admin_cmd(pattern="timp(|n) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="timp(|n) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    catevent = await edit_or_reply(event, f"{name} is ejected.......")
    await asyncio.sleep(2)
    await catevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    if cmd == "":
        await catevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
    elif cmd == "n":
        await catevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was not an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )


CMD_HELP.update(
    {
        "imposter": "**Plugin :** `imposter__`\
\n\n**Syntax : **`.imp` / `.impn` <text>\
\n**Usage : ** Find imposter with stickers.\
\n\n**Syntax : **`.timp` / `.timpn` <text>\
\n**Usage : ** Find imposter only text."
    }
)
