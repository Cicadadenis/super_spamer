import asyncio
import os
import random
from telethon import TelegramClient, Button, events 
from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import Unauthorized

from keyboards.inline.menu import back_admin, admin_menu, choose_menu
from loader import dp, bot
from states.states import BroadcastState, GiveTime, TakeTime
from utils.db_api.db_commands import select_all_users, del_user, update_date
from calendar import c
from email import message
import random
from telethon.sessions import StringSession
from telethon.tl.custom import Button
from datetime import datetime
import asyncio
from keyboards.inline.menu import back_to_main_menu,  api_hash, api_id, code_menu, \
    main_menu, proxy_menu, start_spam_menu, accept_spam_menu
import socks
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputChannel
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import os, sys
import configparser
import csv
import time
import random
#from data.config import api_id, api_hash
#from loader import scheduler
import os
from telethon.sync import TelegramClient
from telethon import functions, types
from datetime import datetime, timedelta

class sms2(StatesGroup):
    sms_text = State()

class post(StatesGroup):
    text = State()

class tima(StatesGroup):
    timeout = State()
@dp.callback_query_handler(text="paussa")
async def paus(call: CallbackQuery):
    await call.message.answer("⏱    <b>Введи значение для паузы между отправкой смс 'меньше 30 сек не рекоминдую спам'</b>")
    @dp.message_handler(content_types=['text'])
    async def paus(message: Message):
        pausse = message.text
        with open('time.txt', 'w') as f:
            f.write(pausse)
        await message.answer(f"⏱    <b>Тайминг Изменен на {pausse}</b>", reply_markup=back_to_main_menu)

@dp.callback_query_handler(text="rep")
async def rep(call: CallbackQuery):
    tt = open('time.txt', 'r')
    ti = int(tt.read())
    tt.close()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    count = int(z)
    i = 0
    s = 0
    c = 0
    o = 0
    msm = 0
    a = 0
    while i <= xx:
        try:
            if a == count:
                await client.disconnect()
                i = i + 1
                a = 0
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            if mm <= 40:
                try:
                    ssm = open('sms.txt', 'r').read()
                    zz = ssm.split('|')
                    sms = random.choice(zz)
                    ss = open('ussers.txt', 'r').readlines()
                    user = ss[a][:-1]
                    print('ok')
                    result = await client(functions.messages.ReportRequest(
                        peer= user,
                        id=[42],
                        reason=types.InputReportReasonSpam(),
                        message='Hello there!'
                    ))
                    await call.message.answer(result)
                    aka = acaunt.split(".")[0]
                    await call.message.answer(
                        f"💬    <b>Жалоба С Акаунта: \n<code>{aka}</code> \nна</b> <code>{user}</code> Отправленна! +1 \n\n")
                    o = o + 1
                    msm = msm + 1
                    mm = mm + 1
                    time.sleep(ti)
                    a = a + 1
                    await client.disconnect()

                except:
                    a = a + 1
                    await call.message.answer(
                        f"💬    <b>Жалоба С Акаунта: \n<code>{aka}</code> \nна</b> <code>{user}</code> Отправленна!\n\n")
                    await client.disconnect()
                    c = c + 1
                    i = i + 1
                    time.sleep(ti)

        except:
            
           
            break
    await call.message.answer(
                        f"💬     <b>Жалобы все отправленны</b> !!", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="sms", state="*")
async def sms(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬    <b>Введи текст для рассылки</b>",
                                 reply_markup=back_to_main_menu)
    await sms2.sms_text.set()
    #await call.message.answer('💬     <b>Текст успешно сохранен</b> !',
     #                     reply_markup=back_to_main_menu)
#
    @dp.message_handler(state=sms2.sms_text)
    async def sms_spam(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open('sms.txt', 'w') as f:
            f.write(sms)
        await message.answer('💬     <b>Текст успешно сохранен</b> !',
                            reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="give_time")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>🆔    Введите ID человека:</b>",
                                               reply_markup=back_admin)
    await GiveTime.GT1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=GiveTime.GT1)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    user_id = message.text
    await message.delete()
    await GiveTime.next()
    await state.update_data(user_id=user_id)
    await msg_to_edit.edit_text("<b>⏰  Введите время в часах которое выдать человеку:</b>", reply_markup=back_admin)


@dp.message_handler(state=GiveTime.GT2)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, user_id = data.get("msg_to_edit"), data.get("user_id")
    try:
        hours = int(message.text)
        await message.delete()
        date_when_expires = datetime.now() + timedelta(hours=hours)
        date_to_db = str(date_when_expires).split(".")[0].replace("-", " ").split(":")
        date_to_db = " ".join(date_to_db[:-1])
        await update_date(user_id, date_to_db)
        await state.finish()
        await msg_to_edit.edit_text("<b>Доступ выдан.</b>", reply_markup=back_admin)
    except ValueError:
        await msg_to_edit.edit_text("<b>    ⏰Не верный формат, попробуйте еще раз.</b>")


@dp.callback_query_handler(text="take_time")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>🆔    Введите ID человека:</b>",
                                               reply_markup=back_admin)
    await TakeTime.T1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=TakeTime.T1)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    user_id = message.text
    await message.delete()
    await update_date(user_id, None)
    await state.finish()
    await msg_to_edit.edit_text("<b>У юзера больше нет доступа.</b>", reply_markup=back_admin)


# ========================BROADCAST========================
# ASK FOR PHOTO AND TEXT
@dp.callback_query_handler(text="broadcast")
async def broadcast2(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("🏞    <b>Отправь фото  которое будут рассылаться по юзерам</b>", reply_markup=back_to_main_menu)
    await BroadcastState.BS1.set()


# RECEIVE PHOTO OR TEXT
@dp.message_handler(content_types=['photo'], state=BroadcastState.BS1)
async def broadcast4(message: Message, state: FSMContext):
    await message.delete()
    easy_chars = 'abcdefghijklnopqrstuvwxyz1234567890'
    name = 'cicada'
    photo_name = name + ".jpg"
    await message.photo[-1].download(f"pics/broadcast/{photo_name}")
    await state.update_data(photo=photo_name, text=message.caption)
    await asyncio.sleep(2)
    await message.answer("🏞    <b>Фото успешно загруженно</b>", reply_markup=back_to_main_menu)



@dp.callback_query_handler(text="fdel")
async def fdel(call: CallbackQuery):
    try:
        path = f'pics/broadcast/cicada.jpg'
        os.remove(path)
        await call.message.answer("<b>Фото Удаленно</b>", reply_markup=back_to_main_menu)
    except:
        await call.message.answer("<b>Фото Удаленно</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="hahah")
async def broadcast_text_post(call: CallbackQuery):
    try:
        kart = os.listdir("pics/broadcast")
        if kart[0] == 'cicada.jpg':
            path = f'pics/broadcast/cicada.jpg'
            with open(path, 'rb') as f:
                photo = f.read()
            ssm = open('sms.txt', 'r').read()
            zz = ssm.split('|')
            sms = random.choice(zz)
            await call.message.answer_photo(photo=photo, caption=f"{ssm}\n\n"
                                                            f"<b>Все правильно? Отправляем?</b>",
                                    reply_markup=choose_menu)
    except:
        ssm = open('sms.txt', 'r').read()
        zz = ssm.split('|')
        sms = random.choice(zz)
        await call.message.answer(ssm + "\n\n<b>Все правильно? Отправляем?</b>", reply_markup=choose_menu)

from telethon import TelegramClient, sync

@dp.callback_query_handler(text="STOP")
async def st(call: CallbackQuery):
    with open("status.txt", "w") as f:
        f.write("1")

# START BROADCAST
@dp.callback_query_handler(text="go_start")
async def broadcast_text_post(call: CallbackQuery):
    path = f'pics/broadcast/cicada.jpg'
    try:
        with open(path, 'rb') as f:
            photo = f.read()
    except:pass
    ti = open('time.txt', 'r').read()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    if z <= 1:
        await call.answer("Добать получателей список пуст !")
        
    count = int(z)
    i = 0
    d = 0
    s = 0
    c = 0
    o = 0
    msm = 0
    a = 0
    v = -1
    while i <= xx:
        try:
            if v == z:
                break
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            if mm <= 40:
                
                try:
                    ssm = open('sms.txt', 'r').read()
                    zz = ssm.split('|')
                    sms = random.choice(zz)
                    ss = open('ussers.txt', 'r').readlines()
                    user = ss[a][:-1]
                    #me = await client.get_me()
                    akk = acaunt.split(".")[0]
                    await client.send_file(ss[a][:-1], file=photo, caption=sms)
                    await call.message.edit_text(
                                f"✉️    <b>Рассылка с Акаунта:</b>    \n<code>{akk}</code>\n"
                                f"<b>На пользователя 🗣 {user} ✅</b>\n\n"
                                f"🛑    <b>Пауза между смс:</b>   <code>{ti} сек</code>\n"
                                f"<b>❌     Недоставленно:  {c}</b>\n"
                                f"<b>✅     Доставленно:    {o}</b>")
                    o = o + 1
                    msm = msm + 1
                    mm = mm + 1
                    v = v + 1
                    time.sleep(ti)
                    a = a + 1
                    d = d + 1
                    
                    
                except:
                    d = d + 1
                    a = a + 1
                    c = c + 1
                    v = v + 1
                    akk = acaunt.split(".")[0]
                    await call.message.edit_text(
                                f"✉️    <b>Рассылка с Акаунта:</b>    \n<code>{akk}</code>\n"
                                f"<b>На пользователя 🗣 {user} ✅</b>\n\n"
                                f"🛑    <b>Пауза между смс:</b>   <code>{ti} сек</code>\n"
                                f"<b>❌     Недоставленно:  {c}</b>\n"
                                f"<b>✅     Доставленно:    {o}</b>")
                    time.sleep(1)
                    
                                         
                    

        except:
            break
    
            

            
    await call.message.answer("✅ <b>Рассылка Завершена</b> ✅", reply_markup=back_to_main_menu)
            

@dp.callback_query_handler(text="ceker")
async def broadcast_text_post(call: CallbackQuery, state: FSMContext):
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581" 
    file_list = os.listdir('sessions')
    xx = len(file_list)   
    i = 0
    s = 0
    a = 0
    tit = 0 
    r = 0
    while i <= xx:
        try:
            mm = 0         
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
           
                    
            
            try:
                #me = await client.get_me()
                await client.send_message('me', 'Hello to myself!')
                time.sleep(1)
                akk = acaunt.split(".")[0]
                await call.message.answer(f"<b>Акаунт {akk}</b> ✅")
               
                i = i + 1
                r = r + 1
                
            except:
                
                path = (f"sessions/{acaunt}")
                os.remove(path)
                tit = tit + 1
                time.sleep(1)
                await call.message.answer(f"<b>Акаунт {akk}</b> ❌")
                i = i + 1   
                                 
                        
        except:
            break
            
    await call.message.answer(
                            f"🔍    <b>Проверка Завершена</b> !\n\n"
                            f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
                            f"❌    <b>В Спаме:  {tit}</b>\n", reply_markup=back_to_main_menu) 
            #break
        

        
              

        




# CANCEL BROADCAST
@dp.callback_query_handler(text="xxx")
async def exitt(call: CallbackQuery):
    await call.message.edit_text("<b>меню</b>", reply_markup=back_to_main_menu)
