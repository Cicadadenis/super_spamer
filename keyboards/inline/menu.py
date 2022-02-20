from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import *

# =========================================================
# ========================MAIN MENU========================
from utils.db_api.db_commands import select_user_accounts, select_user



async def main_menu(user_id):
    user = await select_user(user_id)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✔️ Добавить",
                                     callback_data="adaka"),
                InlineKeyboardButton(text="➖Удалить", callback_data="del_acc")
            ],

            [
                InlineKeyboardButton(text="🔎 Проверка Акаунтов 🔍", callback_data="ceker")
            ],
            [
                InlineKeyboardButton(text="📩 Текст смс", callback_data="sms"),
                InlineKeyboardButton(text="🏞 Загрузить Фото", callback_data="broadcast")
            ],

            [

                InlineKeyboardButton(text="📝 Работа со Списком", callback_data="use"),
                InlineKeyboardButton(text="🗑Удалить фото", callback_data="fdel")
            ],

            [
                InlineKeyboardButton(text="⏱ Тайминг", callback_data="paussa"),
                InlineKeyboardButton(text="🧬 Снос контактов", callback_data="rep")
            ],

            [
                InlineKeyboardButton(text="Парсинг", callback_data="sbor")
            ],
            #[
            #    InlineKeyboardButton(text=f"{'✅' if user[6] == 1 else '⛔️'}Выходить после спам атаки",
             #                        callback_data="leave")
            #],
            [
                InlineKeyboardButton(text="🚀Запустить", callback_data="go_start")
                #InlineKeyboardButton(text="⛔️Остановить", callback_data="stop_spam")
            ],

            #[
            #    InlineKeyboardButton(text="📝Изменить фото", callback_data=f"ed`photo`{chat_id}"),
            #    InlineKeyboardButton(text="🗑Удалить", callback_data=f"ed`del`{chat_id}")
            #],
#
            #[
            #    InlineKeyboardButton(text="🔕Рассылка выключена" if is_on == 0 else "🔔Рассылка включена",
            #                         callback_data=f"ed`turn`{chat_id}")
            #],

 

        ]
    )
    return keyboard




goo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💣 Начать 💣", callback_data="back_to_main_menu")
        ]
    ]
)


akiy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✔️ Добавить по номеру", callback_data="add_account"),
            InlineKeyboardButton(text="✔️ Загрузить sessions", callback_data="ad_sesion")
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)



userrs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📋 Посмотреть список", callback_data="spisok_us"),
            InlineKeyboardButton(text="📥 Загрузить список", callback_data="usse")
        ],

        [
            InlineKeyboardButton(text="➕ Добавить в список", callback_data="adusse"),
            InlineKeyboardButton(text="➖ Удалить из списока", callback_data="rmusse")
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)
# ========================PERSONAL ACCOUNT========================
# MAIN PERSONAL ACCOUNT MENU
personal_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📥Пополнить баланс📥", callback_data="deposit")
        ],
        [
            InlineKeyboardButton(text="📖Все заказы", callback_data="my_orders"),
            InlineKeyboardButton(text="📖Статус заказа", callback_data="show_order_status")
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)

code_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="code_number:1"),
            InlineKeyboardButton(text="2️⃣", callback_data="code_number:2"),
            InlineKeyboardButton(text="3️⃣", callback_data="code_number:3"),
        ],
        [
            
            InlineKeyboardButton(text="4️⃣", callback_data="code_number:4"),
            InlineKeyboardButton(text="5️⃣", callback_data="code_number:5"),
            InlineKeyboardButton(text="6️⃣", callback_data="code_number:6")
        ],
        [
            
            InlineKeyboardButton(text="7️⃣", callback_data="code_number:7"),
            InlineKeyboardButton(text="8️⃣", callback_data="code_number:8"),
            InlineKeyboardButton(text="9️⃣", callback_data="code_number:9")
        ],
        [
            InlineKeyboardButton(text="0️⃣", callback_data="code_number:0")
            
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)

start_spam_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💬 В чат", callback_data="spam:chat"),
            InlineKeyboardButton(text="💌 В лс", callback_data="spam:user")
        ],
        [
            InlineKeyboardButton(text="🤖В бота", callback_data="spam:bot")
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)
STOP = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⛔️Остановить", callback_data="STOP")
        ]
    ]
)
proxy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✔️Добавить", callback_data="add_proxy"),
            InlineKeyboardButton(text="❗️Удалить", callback_data="del_proxy")
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)

accept_spam_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀Запустить атаку", callback_data="accept_spam"),
        ],
        [
            InlineKeyboardButton(text="✖️Отмена", callback_data="back_to_main_menu")
        ]
    ]
)

# =========================================================
# ========================ADMIN MENU========================
# MAIN ADMIN MENU
admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📮Рассылка", callback_data="broadcast")
        ],
        [
            InlineKeyboardButton(text="✅Выдать доступ", callback_data="give_time"),
            InlineKeyboardButton(text="⛔️Забрать доступ", callback_data="take_time")
        ],
        [
            InlineKeyboardButton(text="🔙В главное меню", callback_data="back_to_main_menu")
        ]
    ]
)

# BACK TO ADMIN MENU BUTTON
back_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_admin")
        ]
    ]
)

# DELETE BROADCAST MESSAGE
broadcast_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❇️Понял❇️", callback_data="delete_this_message")
            #"delete_this_message")
        ]
    ]
)

# BROADCAST CONFIRM MENU
choose_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Да", callback_data="yes")
        ],
       # [
        #    InlineKeyboardButton(text="❌Нет", callback_data="xxx")
        #]
    ]
)

# ========================BACK TO MAIN MENU BUTTON========================
back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_to_main_menu")
        ]
    ]
)


# ========================CHATS MENU========================
# ALL USER CHATS
async def accounts_menu(user_id):
    accs = await select_user_accounts(user_id)
    keyboard = InlineKeyboardMarkup(row_width=2)
    for acc in accs:
        keyboard.insert(InlineKeyboardButton(text=acc[1], callback_data=f"accounts:{acc[1]}"))
    keyboard.add(InlineKeyboardButton(text="➕ Добавить аккаунт", callback_data="add_account"))
    keyboard.add(InlineKeyboardButton(text="🔙Назад", callback_data=f"back_to_main_menu"))
    return keyboard


# INSIDE CHAT
def in_chat_menu(is_on, chat_id, number):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📝Изменить текст🔰", callback_data=f"ed`text`{chat_id}"),
                InlineKeyboardButton(text="📝Изменить задержку", callback_data=f"ed`delay`{chat_id}")
            ],
            [
                InlineKeyboardButton(text="📝Изменить фото", callback_data=f"ed`photo`{chat_id}"),
                InlineKeyboardButton(text="🗑Удалить", callback_data=f"ed`del`{chat_id}")
            ],
            [
                InlineKeyboardButton(text="🔕Рассылка выключена" if is_on == 0 else "🔔Рассылка включена",
                                     callback_data=f"ed`turn`{chat_id}")
            ],
            [
                InlineKeyboardButton(text="⬅️Назад", callback_data=f"accounts:{number}")
            ]
        ]
    )
    return keyboard
