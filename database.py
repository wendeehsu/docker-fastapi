from config import db_config


connection = None


async def init_pool():
    global connection

    if db_config.vendor.lower() == 'mysql':
        import asyncio
        import aiomysql
        connection = await aiomysql.connect(
            host=db_config.host,
            port=db_config.port,
            user=db_config.username,
            password=db_config.password,
            db=db_config.db_name,
            loop=asyncio.get_running_loop(),
        )
    elif db_config.vendor.lower() == 'postgresql':
        import asyncpg
        connection = await asyncpg.connect(
            host=db_config.host,
            port=db_config.port,
            user=db_config.username,
            password=db_config.password,
            database=db_config.db_name,
        )
    else:
        raise ValueError


async def shutdown_pool():
    global connection

    if db_config.vendor.lower() == 'mysql':
        await connection.ensure_closed()
    elif db_config.vendor.lower() == 'postgresql':
        await connection.close()
    else:
        raise ValueError
