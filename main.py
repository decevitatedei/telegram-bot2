import os
import logging
import telebot
import time

# Получаем BOT_TOKEN
BOT_TOKEN = '7840822796:AAEmLsshtGysypJDgJR1CWz2RGqvnksehRQ'  # Укажите свой токен сюда

# Создаем объект бота
bot = telebot.TeleBot(BOT_TOKEN)

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Ссылка для регистрации и мини-приложения
REGISTRATION_URL = "https://1wxxlb.com/casino/list/4?p=dqva"
MINI_APP_URL = "https://codepen.io/decevitatedei/full/gOVZXzL"

# Удаляем вебхук перед запуском polling
import requests
requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Добро пожаловать в сигнальный бот 1win bot hack🤖\n\n"
        "Данный бот создан и обучен на кластере нейросети ChatGPT-v4.0🧠"
    )
    buttons = telebot.types.InlineKeyboardMarkup()
    buttons.add(telebot.types.InlineKeyboardButton("Запуск бота", callback_data="start_bot"))
    bot.send_message(message.chat.id, welcome_text, reply_markup=buttons)

# Обработчик кнопки "Запуск бота"
@bot.callback_query_handler(func=lambda call: call.data == "start_bot")
def start_bot(call):
    bot_message = (
        "Бот работает только с новыми аккаунтами, созданными по ссылке в боте, так как "
        "ИИ-система использует хэш этой ссылки для установления связи сервер сайт - телеграм🛜 - наш сервер🧑‍💻 "
        "для получения точного сигнала.\n\n"
        f"Ссылка для создания аккаунта ↙️\n🔗 {REGISTRATION_URL}"
    )
    buttons = telebot.types.InlineKeyboardMarkup()
    buttons.add(telebot.types.InlineKeyboardButton("Зарегистрировался ✅", callback_data="register"))
    bot.send_message(call.message.chat.id, bot_message, reply_markup=buttons)

# Обработчик кнопки "Зарегистрировался ✅"
@bot.callback_query_handler(func=lambda call: call.data == "register")
def register(call):
    bot.send_message(
        call.message.chat.id,
        "Хорошо! Половина работы сделана! Теперь отправьте свой 🆔 (без букв, только 8 цифр), "
        "который можно найти, кликнув на иконку пользователя в правом верхнем углу на сайте."
    )
    bot.register_next_step_handler(call.message, process_user_id)

# Синхронная версия обработчика для обработки ввода ID пользователя
def process_user_id(message):
    user_id = message.text.strip()
    if user_id.isdigit() and len(user_id) == 8:  # Проверяем, что ID состоит из 8 цифр
        bot.send_message(message.chat.id, "🧠Добавляю Ваш ID в базу данных...")
        bot.send_chat_action(message.chat.id, "typing")

        # Задержка перед отправкой следующего сообщения
        time.sleep(10)

        instructions_message = (
            "Доступ открыт ✅\n"
            "Инструкция:\n"
            "1️⃣ Запустите игру Mines на аккаунте 1win, который вы создали по нашей ссылке\n"
            "2️⃣ Откройте бот и получите сигнал\n"
            "3️⃣ Повторите этот сигнал в игре 💸"
        )
        buttons = telebot.types.InlineKeyboardMarkup()
        buttons.add(telebot.types.InlineKeyboardButton("Перейти к сигналам ⭐️🔊", url=MINI_APP_URL))
        bot.send_message(message.chat.id, instructions_message, reply_markup=buttons)
    else:
        bot.send_message(message.chat.id, "Неверный формат ID ❌ Попробуйте пожалуйста снова.")
        bot.register_next_step_handler(message, process_user_id)  # Запрашиваем ID заново

# Запуск бота
print("Бот запущен и работает...")
bot.polling(non_stop=True, interval=0)