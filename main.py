import telebot
import random
from env import TOKEN


bot = telebot.TeleBot(TOKEN)

key_bord = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('/start')
button2 = telebot.types.KeyboardButton('YES')
button3 = telebot.types.KeyboardButton('No')


key_bord.add(button1, button2, button3)

@bot.message_handler(commands=['start', 'hi'])
def star_func(message):
    # print(message.chat.id)
    msg = bot.send_message(message.chat.id, f'привет {message.chat.first_name}, начнём игру', reply_markup=key_bord)
    bot.register_next_step_handler(msg, answer_chak)
    # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJKlmOhP5F0ZvvG29yr0ylhvu8hIV5MAAJhAQAClp-MDqNR4ucv8dmpLAQ')
    # bot.send_photo(message.chat.id, '')

def answer_chak(msg):
    if msg.text == 'YES':
        bot.send_message(msg.chat.id, 'угадай число от 1 до 10, максимум за 3 попытки')
        rand_num = random.randint(1,10)
        p = 3
        start_game(msg, rand_num, p)
    else:
        bot.send_message(msg.chat.id, 'fuck you')

def start_game(msg, rand_num, p):
    msg = bot.send_message(msg.chat.id, 'введи число от 1 до 10')
    bot.register_next_step_handler(msg, check_func, rand_num, p - 1)

def check_func(msg, rand_num, p):
    if msg.text == str(rand_num):
        bot.send_message(msg.chat.id, 'Красавчик')
    elif int(msg.text) >= 10:
        bot.send_message(msg.chat.id, 'я тебе сказал от 1 до 10 долбаёбина')
    elif p == 0:
        bot.send_message(msg.chat.id, 'неудачник, пошёл нахуй отсуда')
    else:
        bot.send_message(msg.chat.id, f'плохо, пробуй ещё, у тебя осталось {p} попыток')
        start_game(msg, rand_num, p)

bot.polling()


# git init
# git add .
# git commite -m 'comment'
# git remote add origin sshKey
# git push origin master