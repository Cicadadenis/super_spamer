import random
from datetime import datetime
import asyncio

import socks
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputChannel
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os, sys
import configparser
import csv
import time
from data.config import api_id, api_hash
from loader import scheduler
from utils.db_api.db_commands import select_user, select_user_proxy, select_user_accounts, update_messages_count


async def send_message_to_chat(user_id, chat_url, msg_txt, photo=None):
    proxies = await select_user_proxy(user_id)
    accounts = await select_user_accounts(user_id)
    for acc in accounts:
        try:
            if proxies:
                proxy_db = random.choice(proxies)[1].split(":")
                proxy = (socks.SOCKS5, proxy_db[1].split(":")[0], int(proxy_db[1].split(":")[1]),
                         proxy_db[0].split(":")[0], proxy_db[0].split(":")[1])
                proxy = (socks.SOCKS5, proxy_db[0], int(proxy_db[1]))
                client = TelegramClient(f"sessions/{acc[1]}", api_id, api_hash, proxy=proxy)
            else:
                client = TelegramClient(f"sessions/{acc[1]}", api_id, api_hash)
            await client.connect()
            if "joinchat" in chat_url:
                try:
                    await client(ImportChatInviteRequest(chat_url.split("/")[-1]))
                except Exception:
                    pass
            else:
                try:
                    await client(JoinChannelRequest(chat_url))
                except Exception:
                    pass
            if photo:
                chats = []
                last_date = None
                chunk_size = 200
                groups=[]

                result = client(GetDialogsRequest(
                                offset_date=last_date,
                                offset_id=0,
                                offset_peer=InputPeerEmpty(),
                                limit=chunk_size,
                                hash = 0
                            ))
                chats.extend(result.chats)

                for chat in chats:
                    try:
                        if chat.megagroup== True:
                            groups.append(chat)
                    except:
                        continue

                print('[+] Выберите группу, чтобы спиздить участников :')
                i=0
                for g in groups:
                    print('['+str(i)+']'+' - '+ g.title)
                    i+=1

                print('')
                g_index = input("[+] Введите номер : ")
                target_group=groups[int(g_index)]

                print('[+] Выборка участников...')
                
                all_participants = []
                all_participants = client.get_participants(target_group, aggressive=True)
                print('[+] Сохранение в файл...')
                time.sleep(2)
                with open("members.csv","w",encoding='UTF-8') as f:
                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
                    for user in all_participants:
                        if user.username:
                            username= user.username
                        else:
                            username= ""
                        if user.first_name:
                            first_name= user.first_name
                        else:
                            first_name= ""
                        if user.last_name:
                            last_name= user.last_name
                        else:
                            last_name= ""
                        name= (first_name + ' ' + last_name).strip()
                        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
                print('[+] Участники успешно сохранены.')
                #await client.send_message(chat_url, msg_txt, file=photo, parse_mode="HTML")
            else:
                await client.send_message(chat_url, msg_txt, parse_mode="HTML")
            await update_messages_count()
            await client.disconnect()
        except Exception:
            await client.disconnect()


async def send_message_to_user(username, message_text, number):
    client = TelegramClient(f"sessions/{number}", api_id, api_hash)
    await client.connect()
    await client.send_message(username, message_text)
    await client.disconnect()
    await asyncio.sleep(2)


async def disconnect_client(number):
    client = TelegramClient(f"sessions/{number}", api_id, api_hash)
    await client.disconnect()


async def stop_job(user_id):
    job = scheduler.get_job(job_id=str(user_id))
    job.remove()


async def get_valid_date(user):
    date_list = user[3].split(" ")
    date_list = list(map(int, date_list))
    date_when_expired = datetime(date_list[0], date_list[1], date_list[2], date_list[3], date_list[4])
    return date_when_expired


async def get_user_date(user_id):
    user = await select_user(user_id)
    now_date = datetime.now()
    if user[3]:
        date_list = user[3].split(" ")
        date_list = list(map(int, date_list))
        date_when_expired = datetime(date_list[0], date_list[1], date_list[2], date_list[3], date_list[4])
        result_date = str(date_when_expired - now_date).split(".")[0].replace("days", "дня/дней").replace("day", "день")
    else:
        result_date = "00:00"

    return result_date
