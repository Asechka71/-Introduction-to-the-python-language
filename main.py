# Прикрутить бота к задаче про конфеты:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

import telebot
from telebot import types
from random import randint
import token

bot = telebot.TeleBot(token)

cell = [' ' for x in range(0,29)]
xorz = 'player'
user_id = ''
sum_candy = 0

def board(cell):
    xorz_board = telebot.types.InlineKeyboardMarkup()
    xorz_board.row(telebot.types.InlineKeyboardButton(f'{cell[1]}', callback_data='1'),
        telebot.types.InlineKeyboardButton(f'{cell[2]}', callback_data='2'),
        telebot.types.InlineKeyboardButton(f'{cell[3]}', callback_data='3'),
        telebot.types.InlineKeyboardButton(f'{cell[4]}', callback_data='4'),
        telebot.types.InlineKeyboardButton(f'{cell[5]}', callback_data='5'),
        telebot.types.InlineKeyboardButton(f'{cell[6]}', callback_data='6'),
        telebot.types.InlineKeyboardButton(f'{cell[7]}', callback_data='7'))
    xorz_board.row(telebot.types.InlineKeyboardButton(f'{cell[8]}', callback_data='8'),
        telebot.types.InlineKeyboardButton(f'{cell[9]}', callback_data='9'),
        telebot.types.InlineKeyboardButton(f'{cell[10]}', callback_data='10'),
        telebot.types.InlineKeyboardButton(f'{cell[11]}', callback_data='11'),
        telebot.types.InlineKeyboardButton(f'{cell[12]}', callback_data='12'),
        telebot.types.InlineKeyboardButton(f'{cell[13]}', callback_data='13'),
        telebot.types.InlineKeyboardButton(f'{cell[14]}', callback_data='14'))
    xorz_board.row(telebot.types.InlineKeyboardButton(f'{cell[15]}', callback_data='15'),
        telebot.types.InlineKeyboardButton(f'{cell[16]}', callback_data='16'),
        telebot.types.InlineKeyboardButton(f'{cell[17]}', callback_data='17'),
        telebot.types.InlineKeyboardButton(f'{cell[18]}', callback_data='18'),
        telebot.types.InlineKeyboardButton(f'{cell[19]}', callback_data='19'),
        telebot.types.InlineKeyboardButton(f'{cell[20]}', callback_data='20'),
        telebot.types.InlineKeyboardButton(f'{cell[21]}', callback_data='21'))
    xorz_board.row(telebot.types.InlineKeyboardButton(f'{cell[22]}', callback_data='22'),
        telebot.types.InlineKeyboardButton(f'{cell[23]}', callback_data='23'),
        telebot.types.InlineKeyboardButton(f'{cell[24]}', callback_data='24'),
        telebot.types.InlineKeyboardButton(f'{cell[25]}', callback_data='25'),
        telebot.types.InlineKeyboardButton(f'{cell[26]}', callback_data='26'),
        telebot.types.InlineKeyboardButton(f'{cell[27]}', callback_data='27'),
        telebot.types.InlineKeyboardButton(f'{cell[28]}', callback_data='28'))
    return xorz_board    

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Начать') 
    markup.add(item1)
    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nДля начала игры в конфеты нажмите на кнопку'.format(message.from_user, bot.get_me()),
        parse_mode = 'html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def menu(message):
    global cell, xorz
    cell = [x for x in range(0,29)]

    if message.text == 'Начать':
        bot.send_message(message.chat.id, f'Сколько конфет берете?{xorz}', reply_markup=board(cell))
    else:
        bot.send_message(message.chat.id, '/start')    

@bot.callback_query_handler(func=lambda call: True)
def callback_fanc(query):
    global cell, user_id, sum_candy, xorz
    data = query.data
    data = int(data) + randint(1,28)

    if sum_candy < 2021:
        user_id = query.from_user.id
        sum_candy = sum_candy + data
        if sum_candy < 2021:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=f'Израсходовано {sum_candy} конфет', reply_markup=board(cell))
    elif sum_candy == 2021:
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=f'Выиграл {user_id}')
        
bot.polling(non_stop=True)    