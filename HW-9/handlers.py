from aiogram import types
from loader import dp
new_game = False
total = 150



@dp.message_handler(commands=['start', 'старт']) 
async def mes_start(message: types.Message):
    print ('Вам пришло сообщение') 
    await message.answer(f'Привет {message.from_user.first_name}, если хочешь поиграть задай количество конфет. '
                         f'для этого набери команду через / set пробел количество конфет'
                         f' После этого нажми на кнопку новая игра /new_game ')



@dp.message_handler(commands=['new_game']) 
async def mes_new_game(message: types.Message):
    global new_game
    new_game = True
    await message.answer('Игра началась')



#/set 200
@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total 
    global new_game
    count = message.text.split()[1]
    if not new_game: 
        if count.isdigit(): 
            total = int(count) 
            await message.answer(f'Конфет теперь будет {count}')
        else:
            await message.answer(f'{message.from_user.first_name}, напишите цифрами')
    else:
        await message.answer(f'{message.from_user.first_name}, нельзя менять правила во время игры!')



@dp.message_handler() 
async def mes_kon(message: types.Message):
    global total
    global new_game
    if new_game: 
        if message.text.isdigit(): 
            total -= int(message.text) 
            if total <= 0:
                await message.answer(f' Ура! {message.from_user.first_name}, ты победил!')
                new_game = False
                    
            else:
                await message.answer(f' {message.from_user.first_name} взял {message.text} конфет '
                                    f'на столе остался {total}') 
            


@dp.message_handler() 
async def mes_all(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, смотри чего поймал - '
                         f'<{message.text}>')