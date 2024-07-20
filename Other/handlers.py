from aiogram import F, Router, types, Bot
from aiogram.types import Message, CallbackQuery, InputFile 
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv


import asyncio
import os
import datetime

import Other.keyboards as kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(f"Welcome to the project Clash Huntercoin, choose language:", reply_markup= kb.choose_language)


'''CALLBACK!'''
@router.callback_query(F.data.startswith('lan_ru'))
async def language_ru (callback:CallbackQuery):
    await callback.message.edit_text(f"Huntercoin доступен для майнинга!", reply_markup=kb.main_ru)
        
@router.callback_query(F.data.startswith('lan_en'))
async def language_ru (callback:CallbackQuery):
    await callback.message.edit_text(f"Huntercoin is available for mining!")
