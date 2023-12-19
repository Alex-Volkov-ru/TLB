from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.requests import get_categories, get_products, get_incomes

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Расходы')],
    [KeyboardButton(text = 'Доходы')],
    [KeyboardButton(text = 'Остаток днежных средств')]
], resize_keyboard=True, input_field_placeholder='Выбери пункт ниже')

async def categories():
    categories_kb = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        categories_kb.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    return categories_kb.adjust(2).as_markup()

async def incomes():
    incomes_kb = InlineKeyboardBuilder()
    incomes = await get_incomes()
    for income in incomes:
        incomes_kb.add(InlineKeyboardButton(text=income.name,callback_data=f'income_{income.id}'))
        return incomes_kb.adjust(2).as_markup()


async def products(category_id):
    products_kb = InlineKeyboardBuilder()
    products = await get_products(category_id)
    for product in products:
        products_kb.add(InlineKeyboardButton(text=product.name, callback_data=f'product_{product.id}'))
    return  products_kb.adjust(2).as_markup()

