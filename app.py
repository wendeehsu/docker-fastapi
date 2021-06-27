import fastapi


app = fastapi.FastAPI()


@app.on_event('startup')
async def app_startup():
    import database
    await database.init_pool()


@app.on_event('shutdown')
async def app_shutdown():
    import database
    await database.shutdown_pool()


@app.get('/')
async def index():
    return "I'm alive!"


@app.get('/insert')
async def insert():
    from database import connection
    import random
    num = random.randint(1, 1000000)
    await connection.execute(f"INSERT INTO my_table (num) VALUES ({num})")

    return f"{num} is inserted!"


@app.get('/read')
async def read():
    from database import connection

    row = await connection.fetchrow("SELECT count(*), min(num), max(num) FROM my_table")
    count, min_num, max_num = row

    return f"There are {count} rows in table, maximum is {max_num}, minimum is {min_num}"
