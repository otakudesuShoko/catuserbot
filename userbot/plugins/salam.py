import asyncio

@bot.on(admin_cmd(outgoing=True, pattern="^P(?: |$)(.*)"))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamualaikum.....`")
    
        
CMD_HELP.update(
    {
            "salam": "__**PLUGIN NAME :** Salam__\
    \n\n📌** CMD ➥** `.p`\
\n**USAGE   ➥  **salam\
