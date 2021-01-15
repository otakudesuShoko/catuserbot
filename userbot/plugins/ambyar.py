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
    
    
@bot.on(admin_cmd(pattern="rindu$", outgoing=True))
@bot.on(sudo_cmd(pattern="rindu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
    event = await edit_or_reply(event, "rindu")
    animation_chars = [
            "`Connecting Ke server Rindu`",
            "`Mencari kabar dia`",
            "`Menahan Rindu..  0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Menahan Rindu.. 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Menahan Rindu.. 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Menahan Rindu.. 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Menahan Rindu.. 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Menahan Rindu.. 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Menahan Rindu.. 84%\n█████████████████████▒▒▒▒ `",
            "`Menahan Rindu. 100%\n█████████RINDUKU███████████ `",
            f"`Ternyata Rindu itu berat, Aku gak kuat biar kamu Saja ajg!!`"]
        for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])
    
    
CMD_HELP.update(
    {
        "ambyar": "__**PLUGIN NAME :** ambyar__\
\n\n**📌 CMD ➥** `.bitch` | `.tidr` | `.skak` | `.rindu ` | \
\n\n**USAGE   ➥  **These are animation bruh..Try & check yourself\
"
    }
)
   
