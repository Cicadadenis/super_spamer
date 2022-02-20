
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
#from data.config import api_id, api_hash
#from loader import scheduler
import os

def cicada():
    api_id = 7265064
    user_id = 1144785510
    api_hash = "9ec54c3437a4b240456f08dd3276f5c3"
    file_list = os.listdir('sessions')
    t = open('time.txt', 'r').read()
    sms = open('sms.txt', 'r').read()
    uss = open('ussers.txt', 'r')
    ff = uss.readlines()
    z = len(ff)
    x = len(file_list)
    i = 0
    pismo = 0
    s = 0
    u = 0
    while i <= z:
        try:
            if pismo >= 40:
                s = s + 1
                pismo = 0
                break
            file_list = os.listdir('sessions')
            acaunt = file_list[s]
            client = TelegramClient(f"sessions/{acaunt}", api_id, api_hash)
            uss = open('ussers.txt', 'r')
            ff = uss.readlines()
            ussers = ff[u][:-1]
            while u <= z:
                ussers = ff[u][:-1]
                print(ussers)
                print(sms)
                client.connect()
                client.send_message(ussers, sms, parse_mode="HTML")
                time.sleep(45)
                client.disconnect()
                print(f'     \nОтправленно {u} sms')
                u = u + 1
            
            break

        except:
            pass

cicada()