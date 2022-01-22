import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

headerss = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
def ex_id(id):
    result = False
    file = open('users.txt', 'r')
    for line in file:
        if line.strip() == id:
            result = True
    return result
token = ''
bot = telebot.TeleBot(token)
create = types.InlineKeyboardButton(text='- صنع استضافه -', callback_data='Create Account 📜')
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == "private":
        if message.chat.type == 'private':
            idd = message.from_user.id
            req = requests.get(f'https://api.telegram.org/bot'+ token +'/getChatMember?chat_id=@rickpro3&user_id='+idd, headers=headerss)
            s = str(req.json()['result']['status'])
            if s == 'left':
                bot.send_message(message.chat.id, text='@rickpro3\nSubscribe to use the bot\n/start')
            else:
                idu = message.from_user.id
                f = open('users.txt', 'a')
                if (not ex_id(str(idu))):
                    usern = message.from_user.username
                    f.write(f"{idu}\n")
                name = message.from_user.first_name
                inline = types.InlineKeyboardMarkup()
                inline.add(create)
                bot.send_message(message.chat.id,text=f'هلا حبيبي {name},\nاضغط على صنع استضافه لصنع استضافه Python',reply_markup=inline)
@bot.message_handler(commands=['count'])
def count(message):
    r = open('users.txt', 'r').read().splitlines()
    bot.send_message(message.chat.id,text="Users : "+str(len(r)))  
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'Create Account 📜':
        create_acc(call.message)
def create_acc(message):
    username = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM') for i in range(12))
    password = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#') for i in range(18))
    email = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM') for i in range(17))
    url = 'https://www.pythonanywhere.com/registration/register/beginner/'
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '256',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'cookie_warning_seen=True; csrftoken=QPldz6eClLRiMvczJ3gRu8FlCP45cbZzoGhc1tOUgsQZ381qvNJk2tXt2KVqfoeZ; sessionid=oag2fm4ea17dklxonpvmq26v93xtzuok; _ga=GA1.1.912772697.1641589928; _gid=GA1.1.1863051091.1641589928; _gat=1',
    'Host': 'www.pythonanywhere.com',
    'Origin': 'https://www.pythonanywhere.com',
    'Referer': 'https://www.pythonanywhere.com/registration/register/beginner/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    }
    data = {
    'csrfmiddlewaretoken': 'X3UhBXp7o52VRzA63M9InnvoGSwZq0uivUQg3kZpjM1C8cpXPwCbVINw6NnktdJI',
    'username': username,
    'email': email+'@gmail.com',
    'password1': password,
    'password2': password,
    'tos': 'on',
    'recaptcha_response_token_v3': '',
    }
    re = requests.post(url,headers=headers,data=data)
    bot.send_message(message.chat.id,text=f'New Account Created✅\n✪━━━━━━━━━━━━━━━━━━━✪\nUsername : {username}\n✪━━━━━━━━━━━━━━━━━━━✪\nEmail : {email}\n✪━━━━━━━━━━━━━━━━━━━✪\nPassword : {password}\n✪━━━━━━━━━━━━━━━━━━━✪\nHost : www.pythonanywhere.com\n✪━━━━━━━━━━━━━━━━━━━✪\nBy : @zzaaz - @rickpro3')

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://omarkk.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
