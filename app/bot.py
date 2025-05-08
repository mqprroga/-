import telebot
from telebot import types

bot = telebot.TeleBot("")

users_list = ["Алексей", "Мария", "Иван"]
users_set = {"Алексей", "Мария", "Иван"}
users_dict = {1: "Алексей", 2: "Мария", 3: "Иван"}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_list = types.KeyboardButton("📋 Список")
    btn_set = types.KeyboardButton("✨ Множество")
    btn_dict = types.KeyboardButton("📖 Словарь")
    markup.add(btn_list, btn_set, btn_dict)
    bot.send_message(message.chat.id, "Выбери структуру данных:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["📋 Список", "✨ Множество", "📖 Словарь"])
def handle_buttons(message):
    if message.text == "📋 Список":
        bot.send_message(message.chat.id, f"Список: {users_list}\nКоманды:\n/add_list [имя]\n/remove_list [имя]")
    elif message.text == "✨ Множество":
        bot.send_message(message.chat.id, f"Множество: {users_set}\nКоманды:\n/add_set [имя]\n/remove_set [имя]")
    elif message.text == "📖 Словарь":
        bot.send_message(message.chat.id, f"Словарь: {users_dict}\nКоманды:\n/add_dict [id] [имя]\n/remove_dict [id]")

@bot.message_handler(commands=['add_list'])
def add_list(message):
    try:
        name = message.text.split()[1]
        users_list.append(name)
        bot.reply_to(message, f"Добавлено: {name}. Теперь список: {users_list}")
    except IndexError:
        bot.reply_to(message, "Ошибка: укажи имя, например: /add_list Анна")

@bot.message_handler(commands=['remove_list'])
def remove_list(message):
    try:
        name = message.text.split()[1]
        users_list.remove(name)
        bot.reply_to(message, f"Удалено: {name}. Теперь список: {users_list}")
    except (IndexError, ValueError):
        bot.reply_to(message, "Ошибка: имя не найдено или не указано")

@bot.message_handler(commands=['add_set'])
def add_set(message):
    try:
        name = message.text.split()[1]
        users_set.add(name)
        bot.reply_to(message, f"Добавлено: {name}. Теперь множество: {users_set}")
    except IndexError:
        bot.reply_to(message, "Ошибка: укажи имя, например: /add_set Анна")

@bot.message_handler(commands=['remove_set'])
def remove_set(message):
    try:
        name = message.text.split()[1]
        users_set.remove(name)
        bot.reply_to(message, f"Удалено: {name}. Теперь множество: {users_set}")
    except (IndexError, KeyError):
        bot.reply_to(message, "Ошибка: имя не найдено или не указано")

@bot.message_handler(commands=['add_dict'])
def add_dict(message):
    try:
        _, id_, name = message.text.split(maxsplit=2)  # Разделяем на 3 части
        users_dict[int(id_)] = name
        bot.reply_to(message, f"Добавлено: {name} (ID: {id_}). Теперь словарь: {users_dict}")
    except (IndexError, ValueError):
        bot.reply_to(message, "Ошибка: используй /add_dict [id] [имя]")

@bot.message_handler(commands=['remove_dict'])
def remove_dict(message):
    try:
        id_ = message.text.split()[1]
        name = users_dict.pop(int(id_))
        bot.reply_to(message, f"Удалено: {name} (ID: {id_}). Теперь словарь: {users_dict}")
    except (IndexError, KeyError):
        bot.reply_to(message, "Ошибка: ID не найден или не указан")

bot.polling()
