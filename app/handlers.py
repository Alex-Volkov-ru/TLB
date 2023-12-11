from aiogram import Router,F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart


import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.main)

@router.message(F.text == 'Расходы')
async def catalog(message: Message):
    await message.answer('Выберите вкладку из категорий ниже', reply_markup=await kb.categories())

@router.callback_query(F.data.startswith('category_'))
async def category_selected(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'Вкладка по выбранной категории', reply_markup= kb.products(category_id))
    await callback.answer('')

@router.callback_query(F.data.startswith('product_'))
async def product_selected(callback: CallbackQuery):
    product_id = callback.data.split('_')[1]
    await callback.message.answer(f'Ваш товар: {product_id}')
    await callback.answer('')

