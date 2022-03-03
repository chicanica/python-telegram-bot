# Телеграм-бот v.002 - бот создаёт меню, присылает собачку, и анекдот

import telebot  # pyTelegramBotAPI	4.3.1
from telebot import types

bot = telebot.TeleBot('5193117811:AAH0hWHVx0kH08sub52IFj2SAdJi1eugY-k')  # Создаем экземпляр бота

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text


    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Задачи")
        btn2 = types.KeyboardButton("Помощь")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)


    elif ms_text == "Задачи":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        btn4 = types.KeyboardButton("4")
        btn5 = types.KeyboardButton("5")
        btn6 = types.KeyboardButton("6")
        btn7 = types.KeyboardButton("7")
        btn8 = types.KeyboardButton("8")
        btn9 = types.KeyboardButton("9")
        btn10 = types.KeyboardButton("10")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, back)
        bot.send_message(chat_id, text="Задачи с 1-го занятия", reply_markup=markup)


    elif ms_text == "1":  # .........................................................
        name = 'Вероника'
        bot.send_message(chat_id, text=name)


    elif ms_text == "2":  # .........................................................
        name = 'Вероника'
        age = 20
        message = 'Привет, меня зовут ' + name + '. Мне ' + str(age) + ' лет.'
        bot.send_message(chat_id, text=message)


    elif ms_text == "3":  # .........................................................
        name = 'Вероника'
        name5 = name*5
        bot.send_message(chat_id, text=name5)


    elif ms_text == "4":  # .........................................................
        bot.send_message(chat_id, text='Ваше имя?')
        @bot.message_handler(content_types=['text'])
        def inputName(message):
            userName = message.text
            bot.send_message(chat_id, text='Сколько Вам лет?')
            @bot.message_handler(content_types=['text'])
            def inputAge(message):
                userAge = message.text
                userMessage = 'Привет, ' + userName + '! Тебе уже ' + userAge + ' лет?! Это так круто!'
                bot.send_message(chat_id, text=userMessage)
            bot.register_next_step_handler(message, inputAge)
        bot.register_next_step_handler(message, inputName)


    elif ms_text == "5":  # .........................................................
        bot.send_message(chat_id, text='Сколько Вам лет?')
        @bot.message_handler(content_types=['text'])
        def inputAge(message):
            userAge = message.text
            userAge = int(userAge)
            if userAge < 18:
                ageMessage = 'Ты не достиг еще совершеннолетия, возращайся позже'
            else:
                ageMessage = 'Ты уже достаточно взрослый, присоединяйся к нам!'
            bot.send_message(chat_id, text=ageMessage)
        bot.register_next_step_handler(message, inputAge)


    elif ms_text == "6":  # .........................................................
        bot.send_message(chat_id, text='Ваше имя?')
        @bot.message_handler(content_types=['text'])
        def inputName(message):
            userName = message.text
            bot.send_message(chat_id, text=userName[1:-1])
            bot.send_message(chat_id, text=userName[::-1])
            bot.send_message(chat_id, text=userName[-3:])
            bot.send_message(chat_id, text=userName[0:5])
        bot.register_next_step_handler(message, inputName)


    elif ms_text == "7":  # .........................................................
        bot.send_message(chat_id, text='Ваше имя?')
        @bot.message_handler(content_types=['text'])
        def inputName(message):
            userName = message.text
            nameMessage = 'Кол-во букв в имени: ' + str(len(userName))
            bot.send_message(chat_id, text=nameMessage)
            bot.send_message(chat_id, text='Сколько Вам лет?')
            @bot.message_handler(content_types=['text'])
            def inputAge(message):
                userAge = message.text
                userAge = int(userAge)
                import math
                ageNum1 = math.floor(userAge / 10)
                ageNum2 = userAge % 10
                sum = ageNum1 + ageNum2
                ageMessage1 = 'Сумма цифр возраста: ' + str(sum)
                bot.send_message(chat_id, text=ageMessage1)
                if ageNum1 < 1:
                    comp = ageNum2
                else:
                    comp = ageNum1 * ageNum2
                ageMessage2 = 'Произведение цифр возраста: ' + str(comp)
                bot.send_message(chat_id, text=ageMessage2)
            bot.register_next_step_handler(message, inputAge)
        bot.register_next_step_handler(message, inputName)


    elif ms_text == "8":  # .........................................................
        bot.send_message(chat_id, text='Ваше имя?')
        @bot.message_handler(content_types=['text'])
        def inputName(message):
            userName = message.text
            bot.send_message(chat_id, text=userName.upper())
            bot.send_message(chat_id, text=userName.lower())
            bot.send_message(chat_id, text=userName.capitalize())
        bot.register_next_step_handler(message, inputName)


    elif ms_text == "9":  # .........................................................
        bot.send_message(chat_id, text='Ваше имя?')
        @bot.message_handler(content_types=['text'])
        def inputName(message):
            userName = message.text
            if " " in userName:
                nameMessage = 'Error userName value'
            else:
                nameMessage = 'Correct userName value'
            bot.send_message(chat_id, text=nameMessage)
            bot.send_message(chat_id, text='Сколько Вам лет?')
            @bot.message_handler(content_types=['text'])
            def inputAge(message):
                userAge = message.text
                userAge = int(userAge)
                if (userAge < 0) or (userAge > 150):
                    ageMessage = 'Error userAge value'
                else:
                    ageMessage = 'Correct userAge value'
                bot.send_message(chat_id, text=ageMessage)
            bot.register_next_step_handler(message, inputAge)
        bot.register_next_step_handler(message, inputName)

    elif ms_text == "10":  # .........................................................
        bot.send_message(chat_id, text='Сколько будет 8+2*3?')
        @bot.message_handler(content_types=['text'])
        def inputAnswer(message):
            userAnswer = message.text
            userAnswer = int(userAnswer)
            if userAnswer == 14:
                userMessage = 'Правильно!'
            else:
                userMessage = 'Неверно!'
            bot.send_message(chat_id, text=userMessage)
        bot.register_next_step_handler(message, inputAnswer)


    elif ms_text == "Помощь" or ms_text == "/help":  # .................................................................
        bot.send_message(chat_id, "Автор: Яковлева Вероника")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/chicanica")
        key1.add(btn1)
        img = open('foto.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)


    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="Вы написали: " + ms_text)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()