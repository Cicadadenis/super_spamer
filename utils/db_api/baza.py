import aiosqlite


#Добавить акаунт
async def add_user(user_id):
    conn = await aiosqlite.connect('db.db', check_same_thread=False)
    await conn.execute("INSERT INTO users (user_id) VALUES(?)", (user_id,))
    await conn.commit()
    await conn.close()



#Выбор Акаунта
async def select_user_accounts(user_id):
    conn = await aiosqlite.connect('db.db', check_same_thread=False)
    cursor = await conn.execute(f"SELECT * FROM accounts WHERE user_id=?", (user_id,))
    h = await cursor.fetchall()
    await conn.close()
    return h
