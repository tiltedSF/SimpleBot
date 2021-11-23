import telebot
from telebot import types
import random
from math import sin
import token

bot = telebot.TeleBot(token.token)

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "мне не интересно", "кто тебя создал?", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\n 1) /cat - присылать котиков \n 2) /music - присылать песенки \n 3) /sin - посчитать синус за тебя')

@bot.message_handler(commands=['cat'])
def start_message(message):
    img_list = ['cats/cat1.jpeg', 'cats/cat2.jpg', 'cats/cat3.jpg', 'cats/cat4.jpg']
    cat = random.choice(img_list)
    img = open(cat, 'rb')
    bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=['music'])
def start_message(message):
    audio = open('music/music.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()

@bot.message_handler(commands=['sin'])
def start_message(message):
    bot.send_message(message.chat.id,"Введи число, синус которого надо найти")

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "мне не интересно":
        bot.send_message(message.chat.id, 'Хорошо, но ты лучше подумай.')
    if message.text.lower() == "кто тебя создал?":
        bot.send_message(message.chat.id, 'Меня создал Петров Дмитрий.')
    if is_number(message.text):
        bot.send_message(message.chat.id, sin(float(message.text)))

bot.polling()