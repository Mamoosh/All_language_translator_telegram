import telepot
import time
import urllib3
import random, time
from googletrans import Translator


#change this values by yours

BOT_TOKEN = ""
ADMIN_ID_NUMBER = 000000000



proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))


bot = telepot.Bot(BOT_TOKEN)

def welcome():
    file = open('start.txt', 'r')
    word = file.read()
    return word

def change(sentense):
    f = open("start.txt", "w")
    f.write(sentense)
    f.close()

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'bg': 'bulgarian',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'tl': 'filipino',
    'fr': 'french',
    'de': 'german',
    'el': 'greek',
    'haw': 'hawaiian',
    'hi': 'hindi',
    'is': 'icelandic',
    'id': 'indonesian',
    'it': 'italian',
    'ja': 'japanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'la': 'latin',
    'lb': 'luxembourgish',
    'mt': 'maltese',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'ro': 'romanian',
    'ru': 'russian',
    'sr': 'serbian',
    'sk': 'slovak',
    'so': 'somali',
    'es': 'spanish',
    'sv': 'swedish',
    'tg': 'tajik',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
}



def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    translator = Translator()
    massage = msg["text"]

    if chat_id == ADMIN_ID_NUMBER and "/change" in massage :
        substring = "/change"
        question = massage
        question = question.replace(substring, '')
        try:
            change(question)
            bot.sendMessage(chat_id, "CHANGED!")
        except:
            bot.sendMessage(chat_id, "ERROR!")
    else:
        answer = ""
        if "/start" in massage :
            pm = welcome()
            bot.sendMessage(chat_id, pm)
        else:
            if len(massage) < 55:
                for language in LANGUAGES.values() :
            
                    question = (translator.translate(massage, dest=language)).text
                    answer = answer + language + " : " + question + "\n"
                bot.sendMessage(chat_id, answer)
            else :
                for language in LANGUAGES.values() :
                    question = (translator.translate(massage, dest=language)).text
                    bot.sendMessage(chat_id, (language + " : " + question))

bot.message_loop(handle)

print('BOT IS ONLINE !')

# Keep the program running.
while 1:
    time.sleep(10)
