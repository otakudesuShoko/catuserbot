# Userbot module to help you manage a group

# Copyright (C) 2019 The Raphielscape Company LLC.
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

from asyncio import sleep

from telethon import functions
from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights, MessageMediaPhoto

from ..utils import errors_handler
from . import BOTLOG, BOTLOG_CHATID, LOGS, get_user_from_event
from .sql_helper.mute_sql import is_muted, mute, unmute

# =================== CONSTANT ===================

PP_TOO_SMOL = "`Gambar ini kecil`"
PP_ERROR = "`Gagal saat memproses gambar`"
NO_ADMIN = "`Anda bukan admin!`"
NO_PERM = "`Anda tidak memiliki izin yang cukup`"
CHAT_PP_CHANGED = "`Gambar group berhasil diganti`"
INVALID_MEDIA = "`Ekstensi Media tidak mendukung`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

# ================================================


@bot.on(admin_cmd(pattern="setgpic$"))
@bot.on(sudo_cmd(pattern="setgpic$", allow_sudo=True))
@errors_handler
async def set_group_photo(gpic):
    if gpic.fwd_from:
        return
    if not gpic.is_group:
        await edit_or_reply(gpic, "`Saya tidak berpikir bahwa ini bukan group.`")
        return
    replymsg = await gpic.get_reply_message()
    await gpic.get_chat()
    photo = None
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split("/"):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await edit_or_reply(gpic, INVALID_MEDIA)
    sandy = None
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await gpic.client.upload_file(photo))
            )
            await edit_or_reply(gpic, CHAT_PP_CHANGED)
            sandy = True
        except PhotoCropSizeSmallError:
            await edit_or_reply(gpic, PP_TOO_SMOL)
        except ImageProcessFailedError:
            await edit_or_reply(gpic, PP_ERROR)
        except Exception as e:
            await edit_or_reply(gpic, f"**Error : **`{str(e)}`")
        if BOTLOG and sandy:
            await gpic.client.send_message(
                BOTLOG_CHATID,
                "#GROUPPIC\n"
                f"Profil group berhasil diganti "
                f"CHAT: {gpic.chat.title}(`{gpic.chat_id}`)",
            )


@bot.on(admin_cmd(pattern="promote(?: |$)(.*)", command="promote"))
@bot.on(sudo_cmd(pattern="promote(?: |$)(.*)", command="promote", allow_sudo=True))
@errors_handler
async def promote(promt):
    if promt.fwd_from:
        return
    if not promt.is_group:
        await edit_or_reply(promt, "`Saya tidak berpikir bahwa ini bukan group.`")
        return
    chat = await promt.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(promt, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    catevent = await edit_or_reply(promt, "`Mempromosikan...`")
    user, rank = await get_user_from_event(promt, catevent)
    if not rank:
        rank = "Anak Haram"
    if not user:
        return
    try:
        await promt.client(EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await catevent.edit("`Berhasil mempromosikan menjadi admin`")
    except BadRequestError:
        await catevent.edit(NO_PERM)
        return
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID,
            "#PROMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {promt.chat.title}(`{promt.chat_id}`)",
        )


@bot.on(admin_cmd(pattern="demote(?: |$)(.*)", command="demote"))
@bot.on(sudo_cmd(pattern="demote(?: |$)(.*)", command="demote", allow_sudo=True))
@errors_handler
async def demote(dmod):
    if dmod.fwd_from:
        return
    if not dmod.is_group:
        await edit_or_reply(dmod, "`Saya tidak berpikir bahwa ini group.`")
        return
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(dmod, NO_ADMIN)
        return
    catevent = await edit_or_reply(dmod, "`Memecat...`")
    rank = "Anak haram"
    user = await get_user_from_event(dmod, catevent)
    user = user[0]
    if not user:
        return
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    try:
        await dmod.client(EditAdminRequest(dmod.chat_id, user.id, newrights, rank))
    except BadRequestError:
        await catevent.edit(NO_PERM)
        return
    await catevent.edit("`Pecat admin berhasil`")
    if BOTLOG:
        await dmod.client.send_message(
            BOTLOG_CHATID,
            "#DEMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {dmod.chat.title}(`{dmod.chat_id}`)",
        )


@bot.on(admin_cmd(pattern="ban(?: |$)(.*)", command="ban"))
@bot.on(sudo_cmd(pattern="ban(?: |$)(.*)", command="ban", allow_sudo=True))
@errors_handler
async def ban(bon):
    if bon.fwd_from:
        return
    if not bon.is_group:
        await edit_or_reply(bon, "`Saya tidak berpikir bahwa ini group.`")
        return
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(bon, NO_ADMIN)
        return
    catevent = await edit_or_reply(bon, "`Jitak pala anak haram !`")
    user, reason = await get_user_from_event(bon, catevent)
    if not user:
        return
    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await catevent.edit(NO_PERM)
        return
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await catevent.edit(
            "`Anda tidak dapat jitak anak haram ini ! Sebab dia sudah diblokir`"
        )
        return
    if reason:
        await catevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)}` is banned !!`\n**Reason : **`{reason}`"
        )
    else:
        await catevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} `is banned !!`"
        )
    if BOTLOG:
        await bon.client.send_message(
            BOTLOG_CHATID,
            "#BAN\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {bon.chat.title}(`{bon.chat_id}`)",
        )


@bot.on(admin_cmd(pattern="unban(?: |$)(.*)", command="unban"))
@bot.on(sudo_cmd(pattern="unban(?: |$)(.*)", command="unban", allow_sudo=True))
@errors_handler
async def nothanos(unbon):
    if unbon.fwd_from:
        return
    if not unbon.is_group:
        await edit_or_reply(unbon, "`Saya tidak berpikir bahwa ini bukan group.`")
        return
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(unbon, NO_ADMIN)
        return
    catevent = await edit_or_reply(unbon, "`Membuka blokir...`")
    user = await get_user_from_event(unbon, catevent)
    user = user[0]
    if not user:
        return
    try:
        await unbon.client(EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await catevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} `is Unbanned Successfully. Granting another chance.`"
        )
        if BOTLOG:
            await unbon.client.send_message(
                BOTLOG_CHATID,
                "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unbon.chat.title}(`{unbon.chat_id}`)",
            )
    except UserIdInvalidError:
        await catevent.edit("`Anak haram gagal di unban!`")


@bot.on(admin_cmd(incoming=True))
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))


@bot.on(admin_cmd(pattern="mute(?: |$)(.*)", command="mute"))
@bot.on(sudo_cmd(pattern="mute(?: |$)(.*)", command="mute", allow_sudo=True))
async def startmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("`Terjadi kesalahan karena faktor face!`")
        await sleep(2)
        await event.get_reply_message()
        userid = event.chat_id
        replied_user = await event.client(GetFullUserRequest(userid))
        chat_id = event.chat_id
        if is_muted(userid, chat_id):
            return await event.edit(
                "`Anak haram ini sudah di bisukan ~~Sampah Telegram~~`"
            )
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit(f"**Error **\n`{str(e)}`")
        else:
            await event.edit("`Berhasil membisukan anak haram.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **`")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#PM_MUTE\n"
                f"**User :** [{replied_user.user.first_name}](tg://user?id={userid})\n",
            )
    else:
        chat = await event.get_chat()
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == bot.uid:
            return await edit_or_reply(
                event, "`Maaf bosku, anda tidak bisa membisukan diri sendiri`"
            )
        if is_muted(user.id, event.chat_id):
            return await edit_or_reply(
                event, "`Anak haram ini sudah di bisukan ~~Sampah Telegram~~~~`"
            )
        try:
            admin = chat.admin_rights
            creator = chat.creator
            if not admin and not creator:
                await edit_or_reply(
                    event, "`Maaf bosku anda tidak bisa membisukan admin .` ಥ﹏ಥ  "
                )
                return
            result = await event.client(
                functions.channels.GetParticipantRequest(
                    channel=event.chat_id, user_id=user.id
                )
            )
            try:
                if result.participant.banned_rights.send_messages:
                    return await edit_or_reply(
                        event,
                        "`Anak haram ini sudah di bisukan ~~Sampah Telegram~~`",
                    )
            except Exception as e:
                LOGS.info(str(e))
            await event.client(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))
        except UserAdminInvalidError:
            if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
                if chat.admin_rights.delete_messages is not True:
                    return await edit_or_reply(
                        event,
                        "`Anda tidak bisa membisukan seseorang karena anda tidak mempunyai izin. ಥ﹏ಥ`",
                    )
            elif "creator" not in vars(chat):
                return await edit_or_reply(
                    event, "`Anda tidak bisa membisukan admin.` ಥ﹏ಥ  "
                )
            try:
                mute(user.id, event.chat_id)
            except Exception as e:
                return await edit_or_reply(event, f"**Error**\n`{str(e)}`")
        except Exception as e:
            return await edit_or_reply(event, f"**Error : **`{str(e)}`")
        if reason:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is muted in {event.chat.title}`\n"
                f"`Reason:`{reason}",
            )
        else:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is muted in {event.chat.title}`\n",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#MUTE\n"
                f"**User :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat :** {event.chat.title}(`{event.chat_id}`)",
            )


@bot.on(admin_cmd(pattern="unmute(?: |$)(.*)", command="unmute"))
@bot.on(sudo_cmd(pattern="unmute(?: |$)(.*)", command="unmute", allow_sudo=True))
async def endmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("`Sorry bosku terjadi kesalahan!`")
        await sleep(1)
        userid = event.chat_id
        replied_user = await event.client(GetFullUserRequest(userid))
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit(
                "`__Anak haram tidak dibisukan di group ini__\n（ ^_^）o自自o（^_^ ）`"
            )
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit(f"**Error **\n`{str(e)}`")
        else:
            await event.edit(
                "`Berhasil membuka akses pesan anak haram\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍`"
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#PM_UNMUTE\n"
                f"**User :** [{replied_user.user.first_name}](tg://user?id={userid})\n",
            )
    else:
        user = await get_user_from_event(event)
        user = user[0]
        if not user:
            return
        try:
            if is_muted(user.id, event.chat_id):
                unmute(user.id, event.chat_id)
            else:
                result = await event.client(
                    functions.channels.GetParticipantRequest(
                        channel=event.chat_id, user_id=user.id
                    )
                )
                try:
                    if result.participant.banned_rights.send_messages:
                        await event.client(
                            EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS)
                        )
                except Exception:
                    return await edit_or_reply(
                        event,
                        "`Anak haram ini sudah bisa mengirim pesan ~~Dasar sampah telegram~~`",
                    )
        except Exception as e:
            return await edit_or_reply(event, f"**Error : **`{str(e)}`")
        await edit_or_reply(
            event,
            f"{_format.mentionuser(user.first_name ,user.id)} `Membuka akses pesan {event.chat.title}\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍`",
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNMUTE\n"
                f"**User :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat :** {event.chat.title}(`{event.chat_id}`)",
            )


@bot.on(admin_cmd(pattern="kick(?: |$)(.*)", command="kick"))
@bot.on(sudo_cmd(pattern="kick(?: |$)(.*)", command="kick", allow_sudo=True))
@errors_handler
async def kick(usr):
    if usr.fwd_from:
        return
    if not usr.is_group:
        await edit_or_reply(usr, "`Saya tidak berpikir bahwa ini group.`")
        return
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(usr, NO_ADMIN)
        return
    user, reason = await get_user_from_event(usr)
    if not user:
        return
    catevent = await edit_or_reply(usr, "`Menendang anak haram...`")
    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(0.5)
    except Exception as e:
        await catevent.edit(NO_PERM + f"\n{str(e)}")
        return
    if reason:
        await catevent.edit(
            f"`Menendang anak haram` [{user.first_name}](tg://user?id={user.id})`!`\nAlasan: {reason}"
        )
    else:
        await catevent.edit(
            f"`Menendang` [{user.first_name}](tg://user?id={user.id})`!`"
        )
    if BOTLOG:
        await usr.client.send_message(
            BOTLOG_CHATID,
            "#KICK\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {usr.chat.title}(`{usr.chat_id}`)\n",
        )


@bot.on(admin_cmd(pattern="pin($| (.*))", command="pin"))
@bot.on(sudo_cmd(pattern="pin($| (.*))", command="pin", allow_sudo=True))
@errors_handler
async def pin(msg):
    if msg.fwd_from:
        return
    if not msg.is_private:
        await msg.get_chat()
    to_pin = msg.reply_to_msg_id
    if not to_pin:
        return await edit_delete(msg, "`Reply pesan untuk menyematkan pesan.`", 5)
    options = msg.pattern_match.group(1)
    is_silent = False
    if options == "loud":
        is_silent = True
    try:
        await msg.client.pin_message(msg.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await edit_delete(msg, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(msg, f"`{str(e)}`", 5)
    await edit_delete(msg, "`Menyematkan pesan berhasil!`", 3)
    user = await get_user_from_id(msg.sender_id, msg)
    if BOTLOG and not msg.is_private:
        try:
            await msg.client.send_message(
                BOTLOG_CHATID,
                "#PIN\n"
                f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {msg.chat.title}(`{msg.chat_id}`)\n"
                f"LOUD: {is_silent}",
            )
        except Exception as e:
            LOGS.info(str(e))


@bot.on(admin_cmd(pattern="unpin($| (.*))", command="unpin"))
@bot.on(sudo_cmd(pattern="unpin($| (.*))", command="unpin", allow_sudo=True))
@errors_handler
async def pin(msg):
    if msg.fwd_from:
        return
    if not msg.is_private:
        await msg.get_chat()
    to_unpin = msg.reply_to_msg_id
    options = (msg.pattern_match.group(1)).strip()
    if not to_unpin and options != "all":
        await edit_delete(
            msg,
            "Reply pesan untuk  membuka pesan sematan group atau gunakan .unpin all`",
            5,
        )
        return
    if to_unpin and not options:
        try:
            await msg.client.unpin_message(msg.chat_id, to_unpin)
        except BadRequestError:
            return await edit_delete(msg, NO_PERM, 5)
        except Exception as e:
            return await edit_delete(msg, f"`{str(e)}`", 5)
    elif options == "all":
        try:
            await msg.client.unpin_message(msg.chat_id)
        except BadRequestError:
            return await edit_delete(msg, NO_PERM, 5)
        except Exception as e:
            return await edit_delete(msg, f"`{str(e)}`", 5)
    else:
        return await edit_delete(
            msg, "`Reply pesan untuk membuka pesan sematan atau gunakan .unpin all`", 5
        )
    await edit_delete(msg, "`Unpinned Successfully!`", 3)
    user = await get_user_from_id(msg.sender_id, msg)
    if BOTLOG and not msg.is_private:
        try:
            await msg.client.send_message(
                BOTLOG_CHATID,
                "#UNPIN\n"
                f"**Admin : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{msg.chat.title}(`{msg.chat_id}`)\n",
            )
        except Exception as e:
            LOGS.info(str(e))


@bot.on(admin_cmd(pattern="iundlt$", command="iundlt"))
@bot.on(sudo_cmd(pattern="iundlt$", command="iundlt", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await edit_or_reply(event, "`Saya tidak berpikir bahwa ini group.`")
        return
    c = await event.get_chat()
    if c.admin_rights or c.creator:
        a = await event.client.get_admin_log(
            event.chat_id, limit=5, edit=False, delete=True
        )
        deleted_msg = "Menghapus pesan di group ini:"
        for i in a:
            deleted_msg += "\n👉`{}`".format(i.old.message)
        await edit_or_reply(event, deleted_msg)
    else:
        await edit_or_reply(
            event, "`Anda harus menjadi admin untuk menggunakan perintah ini`"
        )
        await sleep(3)
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


CMD_HELP.update(
    {
        "admin": "**Plugin : **`admin`\
        \n\n  ➣  **Perintah : **`.setgpic` <Reply gambar>\
        \n  ➣  **Fungsi : **Mengganti profil group\
        \n\n  ➣  **Perintah : **`.promote` <username/reply> <custom jabatan (optional)>\
        \n  ➣  **Fungsi : **Mempromosikan admin.\
        \n\n  ➣  **Perintah : **`.demote `<username/reply>\
        \n  ➣  **Fungsi : **Memecat admin.\
        \n\n  ➣  **Perintah : **`.ban` <username/reply> <reason (optional)>\
        \n  ➣  **Fungsi : **Blokir sesorang dari group.\
        \n\n  ➣  **Perintah : **`.unban` <username/reply>\
        \n  ➣  **Fungsi : **Membuka blokir sesorang.\
        \n\n  ➣  **Perintah : **`.mute` <username/reply> <reason (optional)>\
        \n  ➣  **Fungsi : **Membisukan seseorang.\
        \n\n  ➣  **Perintah : **`.unmute` <username/reply>\
        \n  ➣  **Fungsi : **Membuka akses pesan seseorang.\
        \n\n  ➣  **Perintah : **`.pin `<reply> atau `.pin loud`\
        \n  ➣  **Fungsi : **Menyematkan dengan mereply pesan\
        \n\n  ➣  **Perintah : **`.unpin `<reply> or `.unpin all`\
        \n  ➣  **Fungsi : **Membuka sematan pesan\
        \n\n  ➣  **Perintah : **`.kick `<username/reply> \
        \n  ➣  **Fungsi : **Keluarkan seseorang dari group.\
        \n\n  ➣  **Perintah : **`.iundlt`\
        \n  ➣  **Fungsi : **Menghapus 5 pesan terkahir di group."
    }
)
