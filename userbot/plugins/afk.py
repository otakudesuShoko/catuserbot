# Afk plugin from catuserbot ported from uniborg
import asyncio
from datetime import datetime

from telethon import events
from telethon.tl import Fungsis, types

from . import BOTLOG, BOTLOG_CHATID, bot


class AFK:
    def __init__(self):
        self.USERAFK_ON = {}
        self.afk_time = None
        self.last_afk_message = {}
        self.afk_star = {}
        self.afk_end = {}
        self.reason = None
        self.msg_link = False
        self.afk_type = None
        self.media_afk = None


AFK_ = AFK()


@bot.on(events.NewMessage(outgoing=True))
async def set_not_afk(event):
    if event.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    back_alive = datetime.now()
    AFK_.afk_end = back_alive.replace(microsecond=0)
    if AFK_.afk_star != {}:
        total_afk_time = AFK_.afk_end - AFK_.afk_star
        time = int(total_afk_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        else:
            if h > 0:
                endtime += f"{h}h {m}m {s}s"
            else:
                endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message = event.message.message
    if (("afk" not in current_message) or ("#afk" not in current_message)) and (
        "on" in AFK_.USERAFK_ON
    ):
        shite = await event.client.send_message(
            event.chat_id,
            "`Sappo! Kembali online.\n Setelah Offline selama " + endtime + "`",
        )
        AFK_.USERAFK_ON = {}
        AFK_.afk_time = None
        await asyncio.sleep(5)
        await shite.delete()
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#AFKFALSE \n`Set AFK mode to False\n"
                + "Back alive! No Longer afk.\nWas afk for "
                + endtime
                + "`",
            )


@bot.on(
    events.NewMessage(incoming=True, func=lambda e: bool(e.mentioned or e.is_private))
)
async def on_afk(event):
    if event.fwd_from:
        return
    back_alivee = datetime.now()
    AFK_.afk_end = back_alivee.replace(microsecond=0)
    if AFK_.afk_star != {}:
        total_afk_time = AFK_.afk_end - AFK_.afk_star
        time = int(total_afk_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        else:
            if h > 0:
                endtime += f"{h}h {m}m {s}s"
            else:
                endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text or "#afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if not await event.get_sender():
        return
    if AFK_.USERAFK_ON and not (await event.get_sender()).bot:
        msg = None
        if AFK_.afk_type == "text":
            if AFK_.msg_link and AFK_.reason:
                message_to_reply = (
                    f"**Sappo AFK.\n\nOffline sejak  {endtime}\nAlasan : **{AFK_.reason}"
                )
            elif AFK_.reason:
                message_to_reply = (
                    f"`Sappo AFK .\n\nOffline sejak {endtime}\nAlasan : {AFK_.reason}`"
                )
            else:
                message_to_reply = f"`Sappo afk.\n\nOffline sejak {endtime}"
            if event.chat_id not in Config.UB_BLACK_LIST_CHAT:
                msg = await event.reply(message_to_reply)
        elif AFK_.afk_type == "media":
            if AFK_.reason:
                message_to_reply = (
                    f"`Sappo AFK.\n\nOffline sejak {endtime}\nReason : {AFK_.reason}`"
                )
            else:
                message_to_reply = f"`I am AFK .\n\nAFK Since {endtime}\nReason : Not Mentioned ( ಠ ʖ̯ ಠ)`"
            if event.chat_id not in Config.UB_BLACK_LIST_CHAT:
                msg = await event.reply(message_to_reply, file=AFK_.media_afk.media)
        if event.chat_id in AFK_.last_afk_message:
            await AFK_.last_afk_message[event.chat_id].delete()
        AFK_.last_afk_message[event.chat_id] = msg
        if event.is_private:
            return
        hmm = await event.get_chat()
        if not Config.PM_LOGGER_GROUP_ID:
            return
        full = None
        try:
            full = await event.client.get_entity(event.message.from_id)
        except Exception as e:
            LOGS.info(str(e))
        messaget = media_type(event)
        resalt = f"#AFK_TAGS \n<b>Group : </b><code>{hmm.title}</code>"
        if full is not None:
            resalt += f"\n<b>Dari : </b> 👤{_format.htmlmentionuser(full.first_name , full.id)}"
        if messaget is not None:
            resalt += f"\n<b>Tipe Pesan : </b><code>{messaget}</code>"
        else:
            resalt += f"\n<b>Pesan : </b>{event.message.message}"
        resalt += f"\n<b>Link pesan : </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>"
        if not event.is_private:
            await event.client.send_message(
                Config.PM_LOGGER_GROUP_ID,
                resalt,
                parse_mode="html",
                link_preview=False,
            )


@bot.on(admin_cmd(pattern=r"afk ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    AFK_.USERAFK_ON = {}
    AFK_.afk_time = None
    AFK_.last_afk_message = {}
    AFK_.afk_end = {}
    AFK_.afk_type = "text"
    start_1 = datetime.now()
    AFK_.afk_star = start_1.replace(microsecond=0)
    if not AFK_.USERAFK_ON:
        input_str = event.pattern_match.group(1)
        if ";" in input_str:
            msg, mlink = input_str.split(";", 1)
            AFK_.reason = f"[{msg.strip()}]({mlink.strip()})"
            AFK_.msg_link = True
        else:
            AFK_.reason = input_str
            AFK_.msg_link = False
        last_seen_status = await event.client(
            Fungsis.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            AFK_.afk_time = datetime.now()
        AFK_.USERAFK_ON = f"on: {AFK_.reason}"
        if AFK_.reason:
            await edit_delete(
                event, f"`Offline dulu sappo! Karena ~` {AFK_.reason}", 5
            )
        else:
            await edit_delete(event, f"`Saya harus offline dulu! `", 5)
        if BOTLOG:
            if AFK_.reason:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#AFKTRUE \nSet AFK mode to True, and Reason is {AFK_.reason}",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#AFKTRUE \nSet AFK mode to True, and Reason is Not Mentioned",
                )


@bot.on(admin_cmd(pattern=r"mafk ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    media_t = media_type(reply)
    if media_t == "Sticker" or not media_t:
        return await edit_or_reply(
            event, "`Kamu harus mereply media untuk menggunakan ini`"
        )
    if not BOTLOG:
        return await edit_or_reply(
            event, "`Untuk menggunakan AFK media mohon set PRIVATE_GROUP_BOT_API_ID config`"
        )
    AFK_.USERAFK_ON = {}
    AFK_.afk_time = None
    AFK_.last_afk_message = {}
    AFK_.afk_end = {}
    AFK_.media_afk = None
    AFK_.afk_type = "media"
    start_1 = datetime.now()
    AFK_.afk_star = start_1.replace(microsecond=0)
    if not AFK_.USERAFK_ON:
        input_str = event.pattern_match.group(1)
        AFK_.reason = input_str
        last_seen_status = await event.client(
            Fungsis.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            AFK_.afk_time = datetime.now()
        AFK_.USERAFK_ON = f"on: {AFK_.reason}"
        if AFK_.reason:
            await edit_delete(
                event, f"`Offline dulu sappo! karena ~` {AFK_.reason}", 5
            )
        else:
            await edit_delete(event, f"`Saya harus offline dulu! `", 5)
        AFK_.media_afk = await reply.forward_to(BOTLOG_CHATID)
        if AFK_.reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#AFKTRUE \nSet AFK mode to True, and Reason is {AFK_.reason}",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#AFKTRUE \nSet AFK mode to True, and Reason is Not Mentioned",
            )


CMD_HELP.update(
    {
        "afk": """**Plugin : **`afk`

  **Perintah : **`.mafk [Optional Reason]`
  **Fungsi : **__Menandakan diri anda offline bisa dengan media.__

  **Perintah : **`.afk [Optional Reason]`
  **Fungsi : **__Untuk memberitahukan teman jika anda ingin atau sedang off (Alasan).__

  **Catatan :**Jika kamu ingin Afk Media gunakan [ ; ] Setelah Alasan anda, Kemudian tempel link media anda.
  **Contoh :** `.afk sibuk sekarang ; <Media_link>`

  **Catatan :** __Jika anda memilih untuk tidak afk cukup mengirim pesan__\
        """
    }
)
