# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, 
# добавив в неё систему логирования.

import telebot
import complex_calc

spiterbot = telebot.TeleBot('5726098271:AAEAKWZzWwMjnUtsCOA65FXo8CcnZOzFR_I')

a = -1111
b = -1111
c = -1111
d = -1111
op = ''

@spiterbot.message_handler(commands=['start','help'])
def send_welcome(message):
    spiterbot.reply_to(message,'Для вычислений операций с комплексными числами команда \n/calc')

@spiterbot.message_handler(commands=['calc'])
def send_welcome(message):
    spiterbot.reply_to(message,'введите четыре числа(a,b,c,d) по формату a + bj и c + dj каждое с новой строки, затем операцию +-/*')
    spiterbot.register_next_step_handler(message, type_a)

def type_a(message):
    global a
    while a == -1111:
        try:
            a = int(message.text)
        except Exception:
            spiterbot.send_message(message.from_user.id, 'введите число')
    spiterbot.register_next_step_handler(message, type_b)

def type_b(message):
    global b
    while b == -1111:
        try:
            b = int(message.text)
        except Exception:
            spiterbot.send_message(message.from_user.id, 'введите число')
    spiterbot.register_next_step_handler(message, type_c)

def type_c(message):
    global c
    while c == -1111:
        try:
            c = int(message.text)
        except Exception:
            spiterbot.send_message(message.from_user.id, 'введите число')
    spiterbot.register_next_step_handler(message, type_d)

def type_d(message):
    global d
    while d == -1111:
        try:
            d = int(message.text)
        except Exception:
            spiterbot.send_message(message.from_user.id, 'введите число')
    spiterbot.register_next_step_handler(message, type_op)

def type_op(message):
    global op
    op = message.text
    msg_text_res = complex_calc.calc(complex(a,b),complex(c,d),op)
    spiterbot.send_message(message.from_user.id, msg_text_res)

spiterbot.polling()