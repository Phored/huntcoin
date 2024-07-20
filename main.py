import os
import asyncio

from aiogram import Bot, Dispatcher

from Other.handlers import router

from aiogram.client.session.aiohttp import AiohttpSession

from dotenv import load_dotenv


async def main():
    load_dotenv()
    global bot
    bot=Bot(token=os.getenv('TOKEN'), session=AiohttpSession())
    dp=Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())