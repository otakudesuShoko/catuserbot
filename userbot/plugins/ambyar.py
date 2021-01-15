import asyncio
from collections import deque

from . import mention


@bot.on(admin_cmd(pattern=f"bitch$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"bitch$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "I'M A BROKENT HOME")
    await asyncio.sleep(2)
    await event.edit("👨‍👩‍👦________________🚗_")
    await asyncio.sleep(1)
    await event.edit("👨‍👩‍👦______________🚗___")
    await asyncio.sleep(1)
    await event.edit("👨‍👩‍👦___________🚗______")
    await asyncio.sleep(1)
    await event.edit("👨‍👩‍👦________🚗_________")
    await asyncio.sleep(1)
    await event.edit("👨‍👩‍👦______🚗___________")
    await asyncio.sleep(1)
    await event.edit("👨‍👩‍👦___🚗______________")
    await asyncio.sleep(1)
    await event.edit("👨‍👩‍👦__🚗_______________")
    await asyncio.sleep(1)
    await event.edit("👨‍👩‍👦__🚶🏻‍♂🚗_____________")
    await asyncio.sleep(1)
    await event.edit("👨‍👦🧍🏻‍♀__🚶🏻‍♂🚗____________")
    await asyncio.sleep(1)
    await event.edit("👨‍👦_👫🚗_______________")
    await asyncio.sleep(1)
    await event.edit("👨‍👦💔👫🚗_______________")
    await asyncio.sleep(1)
    await event.edit("👨‍👦💔👩‍❤️‍💋‍👨🚗_______________")
    await asyncio.sleep(1)
    await event.edit("👨‍👦__🚗________________")
    await asyncio.sleep(1)
    await event.edit("👨‍👦_🚗_________________")
    await asyncio.sleep(1)
    await event.edit("_👨‍👦___________________")
    await asyncio.sleep(1)
    await event.edit("_👨‍👦_______🚶🏻‍♀___________")
    await asyncio.sleep(1)
    await event.edit("_👨‍👦__🚶🏻‍♀________________")
    await asyncio.sleep(1)
    await event.edit("_😓__👩‍❤️‍👨________________")
    await asyncio.sleep(1)
    await event.edit("_👫__💔_☹️_______________")
    await asyncio.sleep(1)
    await event.edit("_💔_😔__________________")
    await asyncio.sleep(1)
    await event.edit("🙂Tangisan hanya mengacaukan segalanya tapi senyuman membuat mereka yakin aku Tegar")
    await asyncio.sleep(3)
    await event.edit("☹️Setiap anak ingin keluarga yang sempurna\ntapi tidak semua anak memilikinya.")
    await asyncio.sleep(3)
    await event.edit("Sayangilah kedua orang tuamu dengan\nsepenuh hati selagi masih ada🙂")
    await asyncio.sleep(3)
   
    
@bot.on(admin_cmd(pattern=f"tidr$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"tidr$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**Eh, beban keluarga tdr woi"" ")
    await asyncio.sleep(2)
    await event.edit("**Sadar gadangnya bukan untukmu**")
    await asyncio.sleep(2)
    await event.edit("**Melainkan untuk dia di akun satu**")    
    await asyncio.sleep(2)
    

@bot.on(admin_cmd(pattern=f"tidr$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"tidr$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**Eh, beban keluarga tdr woi"" ")
    await asyncio.sleep(2)
    await event.edit("**Sadar gadangnya bukan untukmu**")
    await asyncio.sleep(2)
    await event.edit("**Melainkan untuk dia di akun satu**")    
    await asyncio.sleep(2)
    
    
@bot.on(admin_cmd(pattern=f"skak$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"skak$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**Hmmm, Gurih-Gurih nyoy"" ")
    await asyncio.sleep(2)
    await event.edit("**Enak kena skak?**")
    await asyncio.sleep(2)
    await event.edit("**Yahahahah mampus lu dajjal😂**")    
    await asyncio.sleep(2)
    
    
CMD_HELP.update(
    {
        "ambyar": "__**PLUGIN NAME :** ambyar__\
\n\n**📌 CMD ➥** `.bitch` | `.tidr` | `.skak` | ` \
\n\n**USAGE   ➥  **These are animation bruh..Try & check yourself\
"
    }
)
   
