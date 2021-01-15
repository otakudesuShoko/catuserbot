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
    await event.edit("🙂Tangisan hanya mengacaukan segalanya tapi senyuman membuat mereka yakin aku Tegar")
    await asyncio.sleep(5)
    await event.edit("☹️Setiap anak ingin keluarga yang sempurna\ntapi tidak semua anak memilikinya.")
    await asyncio.sleep(5)
    await event.edit("Sayangilah kedua orang tuamu dengan\nsepenuh hati selagi masih ada🙂")
    await asyncio.sleep(5)
   
    
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
\n\n**📌 CMD ➥** `.bitch` | `.tidr` | `.skak` | `. \
\n\n**USAGE   ➥  **These are animation bruh..Try & check yourself\
"
    }
)
   
