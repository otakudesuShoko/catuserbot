import asyncio
from collections import deque

from . import mention


@bot.on(admin_cmd(pattern="p$"))
@bot.on(sudo_cmd(pattern="p$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Punten")
    await asyncio.sleep(2)
    await event.edit("Wah rame nih, ehem")
    await asyncio.sleep(2)
    await event.edit("Mau pantun dulu bolehlah")
    await asyncio.sleep(2)
    await event.edit("anak dajjal belajar hukum")
    await asyncio.sleep(2)
    await event.edit("Assalamualaikum")
    await asyncio.sleep(2)
    
    
@bot.on(admin_cmd(pattern="l$"))
@bot.on(sudo_cmd(pattern="l$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Astaga kalian berdosa banget..")
    await asyncio.sleep(2)
    await event.edit("Jaka sembung bawa golok..")
    await asyncio.sleep(2)
    await event.edit("Menjawab salam itu wajib goblok")
    await asyncio.sleep(2)
    await event.edit("Si Asep naik kapal selam..")
    await asyncio.sleep(2)
    await event.edit("Waalaikumsalam ")    
    await asyncio.sleep(2)   
    
 
 CMD_HELP.update(
     [
          "salam": "__**PLUGIN NAME :** salam__\
 \n\n**📌 CMD ➥ `.p` | `.l` | \ 
 \n\n**USAGE   ➥  **Menjawab salam dan salam\
 "
    }
)          
          
