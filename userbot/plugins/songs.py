"""
by  @sandy1709 ( https://t.me/mrconfused  )
"""
# songs finder for catuserbot

import asyncio
import base64
import os
from pathlib import Path

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from . import hmention, name_dl, runcmd, song_dl, video_dl
from . import yt_search as yt_search_no
from . import yt_search_api

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>Sedang mencari lagu yang anda request..</code>"
SONG_NOT_FOUND = "<code>Maaf! Konten lagu tidak ditemukan</code>"
SONG_SENDING_STRING = "<code>Yeah! Lagu sudah ditemukan..</code>"
SONGBOT_BLOCKED_STRING = "<code>Mohon unblok @songdl_bot lalu coba lagi</code>"
# =========================================================== #
#                                                             #
# =========================================================== #


@bot.on(admin_cmd(pattern="(song|song320)($| (.*))"))
@bot.on(sudo_cmd(pattern="(song|song320)($| (.*))", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply:
        if reply.message:
            query = reply.message
    else:
        await edit_or_reply(event, "`Apa yang harus saya cari `")
        return
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catevent = await edit_or_reply(event, "`Sedang mencari lagu yang anda minta...`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(f"Mohon maaf konten tidak dapat ditemukan `{query}`")
    cmd = event.pattern_match.group(1)
    if cmd == "song":
        q = "128k"
    elif cmd == "song320":
        q = "320k"
    song_cmd = song_dl.format(QUALITY=q, video_link=video_link)
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    stderr = (await runcmd(song_cmd))[1]
    if stderr:
        return await catevent.edit(f"**Error :** `{stderr}`")
    catname, stderr = (await runcmd(name_cmd))[:2]
    if stderr:
        return await catevent.edit(f"**Error :** `{stderr}`")
    # stderr = (await runcmd(thumb_cmd))[1]
    catname = os.path.splitext(catname)[0]
    # if stderr:
    #    return await catevent.edit(f"**Error :** `{stderr}`")
    song_file = Path(f"{catname}.mp3")
    if not os.path.exists(song_file):
        return await catevent.edit(f"Mohon maaf konten tidsk ada `{query}`")
    await catevent.edit("`Yeah! Lagu sudah ditemukan..`")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None

    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"<b><i>➥ Lagu :- {query}</i></b>\n<b><i>➥ Hak Cipta :- {hmention}</i></b>",
        thumb=catthumb,
        supports_streaming=True,
        parse_mode="html",
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


async def delete_messages(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)


@bot.on(admin_cmd(pattern="vsong( (.*)|$)"))
@bot.on(sudo_cmd(pattern="vsong( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        if reply.message:
            query = reply.messag
    else:
        event = await edit_or_reply(event, "Apa yang seharusnya saya cari")
        return
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catevent = await edit_or_reply(event, "`Sedang mencari lagu yang anda request..`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(f"Mohon maaf konten tidak ditemukan`{query}`")
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    video_cmd = video_dl.format(video_link=video_link)
    stderr = (await runcmd(video_cmd))[1]
    if stderr:
        return await catevent.edit(f"**Error :** `{stderr}`")
    catname, stderr = (await runcmd(name_cmd))[:2]
    if stderr:
        return await catevent.edit(f"**Error :** `{stderr}`")
    # stderr = (await runcmd(thumb_cmd))[1]
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    # if stderr:
    #    return await catevent.edit(f"**Error :** `{stderr}`")
    catname = os.path.splitext(catname)[0]
    vsong_file = Path(f"{catname}.mp4")
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{catname}.mkv")
    elif not os.path.exists(vsong_file):
        return await catevent.edit(f"Mohon maaf konten tidak ditemukan `{query}`")
    await catevent.edit("`yeah..! i Yeah! Lagu sudah ditemukan..🥰`")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        force_document=False,
        caption=f"<b><i>➥ Lagu :- {query}</i></b>\n<b><i>➥ Hak Cipta :- {hmention}</i></b>",
        thumb=catthumb,
        supports_streaming=True,
        parse_mode="html",
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


async def yt_search(cat):
    videol = None
    try:
        if Config.YOUTUBE_API_KEY:
            vi = await yt_search_api(cat)
            video = f"https://youtu.be/{vi[0]['id']['videoId']}"
    except:
        pass
    if videol is None:
        vi = await yt_search_no(cat)
        video = vi[0]
    return video


@bot.on(admin_cmd(pattern="song2 (.*)"))
@bot.on(sudo_cmd(pattern="song2 (.*)", allow_sudo=True))
async def cat_song_fetcer(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    catevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(song)
            hmm = await conv.get_response()
            while hmm.edit_hide != True:
                await asyncio.sleep(0.1)
                hmm = await event.client.get_messages(chat, ids=hmm.id)
            baka = await event.client.get_messages(chat)
            if baka[0].message.startswith(
                ("I don't like to say this but I failed to find any such song.")
            ):
                await delete_messages(event, chat, purgeflag)
                return await edit_delete(
                    catevent, SONG_NOT_FOUND, parse_mode="html", time=5
                )
            await catevent.edit(SONG_SENDING_STRING, parse_mode="html")
            await baka[0].click(0)
            music = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(SONGBOT_BLOCKED_STRING, parse_mode="html")
            return
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b><i>➥ Lagu :-</i></b> <code>{song}</code>\n<b><i>➥ Hak Cipt :- {hmention}</i></b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await catevent.delete()
        await delete_messages(event, chat, purgeflag)


@bot.on(admin_cmd(pattern="music (.*)"))
@bot.on(sudo_cmd(pattern="music (.*)", allow_sudo=True))
async def kakashi(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@SongsForYouBot"
    link = f"/song {song}"
    catevent = await edit_or_reply(event, "`Sedang mencari lagu yang anda request...`")
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message(link)
            baka = await conv.get_response()
            music = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Please unblock @SongsForYouBot and try again```")
            return
        await catevent.edit("`Mengirim Lagu kamu...`")
        await asyncio.sleep(1.5)
        await catevent.delete()
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b><i>➥ Lagu :- {song}</i></b>\n<b><i>➥ Hak Cipta :- {hmention}</i></b>",
            parse_mode="html",
        )
    await event.client.delete_messages(
        conv.chat_id, [msg_start.id, response.id, msg.id, baka.id, music.id]
    )


@bot.on(admin_cmd(outgoing=True, pattern="dzd (.*)"))
@bot.on(sudo_cmd(outgoing=True, pattern="dzd (.*)", allow_sudo=True))
async def kakashi(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    if ".com" not in link:
        catevent = await edit_or_reply(
            event, "` Saya butuh link untuj mencari lagu.`**(._.)**"
        )
    else:
        catevent = await edit_or_reply(event, "**Sedang download!**")
    chat = "@DeezLoadBot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            r = await conv.get_response()
            msg = await conv.send_message(link)
            details = await conv.get_response()
            song = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
            return
        await catevent.delete()
        await event.client.send_file(event.chat_id, song, caption=details.text)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, response.id, r.id, msg.id, details.id, song.id]
        )


CMD_HELP.update(
    {
        "songs": "__**PLUGIN NAME :** Songs__\
        \n\n📌** CMD ➥** `.song` <query>  or `.song reply to song name`\
        \n**USAGE   ➥  **Searches the song you entered in query and sends it,quality of it is 128k\
        \n\n📌** CMD ➥** `.song320` <query> or `.song320 reply to song name`\
        \n**USAGE   ➥  **Searches the song you entered in query and sends it,quality of it is 320k\
        \n\n📌** CMD ➥** `.vsong` <query> or `.vsong reply to song name`\
        \n**USAGE   ➥  **Searches the video song you entered in query and sends it\
        \n\n📌** CMD ➥** `.song2` <query>\
        \n**USAGE   ➥  **Searches the song you entered in query and sends it.\
        \n\n📌** CMD ➥** `.music` <Artist - Song Title>\
        \n**USAGE   ➥  **Download your music by just name.\
        \n\n📌** CMD ➥** `.dzd` <Spotify/Deezer Link>\
        \n**USAGE   ➥  **Download music from Spotify or Deezer."
    }
)
