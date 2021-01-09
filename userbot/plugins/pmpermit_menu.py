"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio

from telethon import events, functions

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql

from . import PM_START, PMMESSAGE_CACHE, mention, set_key

PREV_REPLY_MESSAGE = {}


@bot.on(events.NewMessage(pattern=r"\/start", incoming=True))
async def _(event):
    if event.fwd_from:
        return
    chat_id = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if chat_id not in PM_START:
            PM_START.append(chat_id)
        if not event.is_private:
            return
        set_key(PMMESSAGE_CACHE, event.chat_id, event.id)
        PM = (
            "Halo. Anda sedang mengakses menu yang tersedia dari tuan saya, "
            f"{mention}.\n"
            "__Mari kita perjelas dan beri tahu saya mengapa Anda ada di sini.__\n"
            "**Pilih salah satu alasan berikut mengapa Anda berada di sini:**\n\n"
            "`a`. Untuk mengobrol dengan tuanku\n"
            "`b`. Untuk mengirim spam ke kotak masuk master saya..\n"
            "`c`. Untuk menanyakan sesuatu\n"
            "`d`. Untuk meminta sesuatu\n"
        )
        ONE = (
            "__Baik, Permintaan Anda telah terdaftar. Jangan mengirim spam ke kotak masuk master saya. Anda dapat mengharapkan balasan dalam waktu 24 Jam.. Dia orang yang sibuk, tidak seperti Anda mungkin.__\n\n"
            "**⚠️ Anda akan diblokir dan dilaporkan jika Anda melakukan spam.. ⚠️**\n\n"
        )
        TWO = " `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**Anjing banget, ini bukan rumah Anda. Ganggu orang lain. Anda telah diblokir dan dilaporkan hingga lebih jauh memperhatikan.**"
        THREE = "__Oke. Tuan saya hUntuk menanyakan sesuatu, belum melihat pesan Anda. Dia biasanya menanggapi orang, meskipun tidak tahu tentang yang diulang.__\n __Dia akan menjawab ketika dia kembali, jika dia mau. Sudah ada banyak pesan yang menunggu keputusan:😶__\n **Harap jangan mengirim spam kecuali Anda ingin diblokir dan dilaporkan..**"
        FOUR = "`Oke, mohon sopan santun agar tidak terlalu mengganggu tuanku. Jika dia ingin membantu kamu, dia akan segera menanggapimu.`\n**Jangan meminta berulang kali karena kamu akan diblokir dan dilaporkan.**"
        LWARN = "**Ini adalah peringatan terakhir Anda. JANGAN kirim pesan lagi karena Anda akan diblokir dan dilaporkan. Tetap sabar, Majikan saya akan membalas Anda secepat mungkin. **\n"
        try:
            async with event.client.conversation(chat) as conv:
                if pmpermit_sql.is_approved(chat_id):
                    return
                test1 = await event.client.send_message(chat, PM)
                set_key(PMMESSAGE_CACHE, event.chat_id, test1.id)
                chat_id = event.sender_id
                response = await conv.get_response(chat)
                y = response.text
                if y == "a" or "A":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test2 = await event.client.send_message(chat, ONE)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test2.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test3 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test3.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test4 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test4.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "b" or "B":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test5 = await event.client.send_message(chat, LWARN)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test5.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test6 = await event.client.send_message(chat, TWO)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test6.id)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "c" or "C":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test7 = await event.client.send_message(chat, THREE)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test7.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test8 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test8.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test9 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test9.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "d" or "D":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test10 = await event.client.send_message(chat, FOUR)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test10.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test11 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test11.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            await event.client.send_message(chat, TWO)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                else:
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    test12 = await event.client.send_message(
                        chat,
                        "You have entered an invalid command. Please send `/start` again or do not send another message if you do not wish to be blocked and reported.",
                    )
                    set_key(PMMESSAGE_CACHE, event.chat_id, test12.id)
                    response = await conv.get_response(chat)
                    z = response.text
                    if z != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test13 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test13.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test14 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test14.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
        except:
            pass
