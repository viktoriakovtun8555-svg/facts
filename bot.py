from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton 
from aiogram.filters import Command
from random import choice
import asyncio 

bot = Bot(token='8760016418:AAHzxqQqR5bYkt_8joLhrrKe8WhA-jN-f2g')
dp = Dispatcher()

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='факти о космосі'), KeyboardButton(text='факти о тваринах')],
        [KeyboardButton(text='факти о погоде'), KeyboardButton(text='факти о снах')]
    ], resize_keyboard=True
)

@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Привіт! Обери факт о якому хочешь узнати', reply_markup=kb)

space = ['У космосі немає звуку бо там майже відсутнє повітря', 'Сліди людей на Місяці Moon можуть зберігатися мільйони років', 'На Марсі Mars заходи Сонця мають блакитний колір']

@dp.message(F.text == 'факти о космосі')
async def cmd_start(message: Message):
    await message.answer(choice(space))

animals = ['Жирафи Giraffe можуть спати лише 30 хвилин на добу', 'Дельфіни Dolphin впізнають себе у дзеркалі', 'Медоїди Honey badger вважаються одними з найсміливіших тварин у світі']

@dp.message(F.text == 'факти о тваринах')
async def cmd_start(message: Message):
    await message.answer(choice(animals))

weather = ['Блискавка може бути гарячішою за поверхню Сонця', 'Урагани можуть тривати більше тижня та охоплювати сотні кілометрів', 'Найсильніші вітри на Землі виникають під час торнадо']

@dp.message(F.text == 'факти о погоде')
async def cmd_start(message: Message):
    await message.answer(choice(weather))

dreams = ['Іноді уві сні люди можуть відчувати запахи, звуки та емоції', 'Найяскравіші сни зазвичай сняться під час швидкої фази сну', 'Людина забуває більшість своїх снів уже через кілька хвилин після пробудження']

@dp.message(F.text == 'факти о снах')
async def cmd_start(message: Message):
    await message.answer(choice(dreams))



async def main():
    await dp.start_polling(bot)

asyncio.run(main())
