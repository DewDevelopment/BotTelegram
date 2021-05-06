import telebot;

bot = telebot.TeleBot('1603377728:AAG2hIYoflH3OQwYJy8JM6bRFn5W8ej-VEQ')
from telebot import types;

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, я Бот-Путешественник, я помогу тебе определиться с выбором страны для путешествия")
      bot.send_message(message.from_user.id, "Выбери страну и я покажу тебе информацию о ней")
      keyboard = telebot.types.InlineKeyboardMarkup()
      key_europe = types.InlineKeyboardButton(text='Европа', callback_data='europe')
      if (key_europe):
        key_spain = types.InLineKeyboardButton(text='Испания')
      key_asia = types.InlineKeyboardButton(text='Азия', callback_data='asia')
      key_america = types.InlineKeyboardButton(text='Америка', callback_data='america')
      key_africa = types.InlineKeyboardButton(text='Африка', callback_data='africa')
      key_australia = types.InlineKeyboardButton(text='Австралия', callback_data='australia')
      keyboard.add(key_europe, key_africa, key_america, key_australia)
      bot.send_message(message.from_user.id, text='Для начала, выбери часть света, куда бы ты хотел отправиться', reply_markup=keyboard)
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши Привет, чтобы я начал работать")  
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    if c.data == "europe":
        bot.send_message(c.message.chat.id, "Вы выбрали Европу")
    elif c.data == "asia":
        bot.send_message(c.message.chat.id, "Вы выбрали Азию")
    elif c.data == "america":
        bot.send_message(c.message.chat.id, "Вы выбрали Америку")
    elif c.data == "africa":
        bot.send_message(c.message.chat.id, "Вы выбрали Африку")
    elif c.data == "australia":
        key = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardMarkup(text="Сидней", callback_data="Num1")
        key_2 = types.InlineKeyboardMarkup(text="Мельбрун", callback_data="Num2")
        key_3 = types.InlineKeyboardMarkup(text="Брисбен", callback_data="Num3")
        key.add(key_1, key_2, key_3)
        bot.send_message(c.message.chat.id, "Вы выбрали Австралию, теперь выберите город", reply_markup=key)
        
bot.polling(none_stop=True, interval=0)
