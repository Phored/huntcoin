from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.types.web_app_info import WebAppInfo

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


choose_language = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🇷🇺 RU", callback_data="lan_ru"), InlineKeyboardButton(text="🇺🇸 EN", callback_data="lan_en")]
])



main_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Открыть" ,web_app=WebAppInfo(url='https://phored.github.io/mintcoin-hunter.io/'))]
])