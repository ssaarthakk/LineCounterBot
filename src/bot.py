import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_KEY")

bot = telebot.TeleBot(API_TOKEN)

message_references = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am LineCounter Bot.🤖\n
I am here to Count the number of lines in your message or remove duplicate lines if you want.\n\nStart by sending me a message.\
""")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Remove duplicate lines?", callback_data="button_click")
    markup.add(button)
    reply_message = bot.reply_to(message, len(message.text.splitlines()), reply_markup=markup)
    message_references[reply_message.message_id] = message.text
    
@bot.callback_query_handler(func=lambda call: call.data == "button_click")
def handle_button_click(call):
    
    original_message = message_references.get(call.message.message_id)
    
    if original_message:
        new_message = set(original_message.lower().splitlines())
        bot.send_message(call.message.chat.id, '\n'.join(new_message))
        bot.answer_callback_query(call.id, "The order of the message might be different from original message!")
    else:
        bot.send_message(call.message.chat.id, "Some error occured!")
        
    if message_references:
        message_references.popitem()

bot.infinity_polling()