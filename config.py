import pymongo
import asyncio
import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from timezonefinder import TimezoneFinder


API_TOKEN = os.environ['daddy_token']
TG_API_ID = int(os.environ['tg_api_id'])
TG_API_HASH = os.environ['tg_api_hash']

loop = asyncio.get_event_loop()

storage = MemoryStorage()
client = pymongo.MongoClient(os.environ['daddy_db'])
db = client.bot_father
collection = db.pin_list

bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)

col2 = db.users
colv = db.veganwars_helper
colh = db.her_morzhovij
col_groups_users = db.groups_and_users
col_sessions = db.sessions
banned = col2.find_one()

developers = [879343317]
bot_user = loop.run_until_complete(bot.get_me())
bot_id = bot_user.id
bot_user = bot_user.username

SERVICE_ACCOUNT_ID = 1096455676

OSM_API = os.environ['OSM_API']
QUOTES_API_TOKEN = os.environ['QUOTES_API_TOKEN']
geotoken = os.environ['geotoken']
tf = TimezoneFinder(in_memory=True)

ban_keywords_list = ('!иди в баню', '!иди в бан', '!банан тебе в жопу', '!нам будет тебя не хватать', '/ban',
                     '/ban@botsdaddyybot', )
unban_keywords_list = ('!мы скучаем', '!выходи из бани', '!кончил', '/unban', '/unban@botsdaddyybot', )
mute_keywords_list = ('!мут', )
unmute_keywords_list = ('!анмут', )
OD_flood_list = ("Да как ты разговариваешь со старшими!", )
ban_mute_list = ban_keywords_list + unban_keywords_list + mute_keywords_list + unmute_keywords_list
hang_bot_flood = {}

compliments = ('ты сегодня такая красивая(ый)!',
               'твои губки напоминают мне сочные вишенки, за которые хочется укусить ~_~',
               'привет, ты с какой звезды детка',
               'даа, покажи мне свои мускулы, они такие красивыее',
               'твои волосы такие прекрасные, как ты за ними ухаживаешь?')

COMMANDS = ('/pin - pin a message, /pin 1 to pin silently \n'
            '/pintime - pin a message several time (/pintime x), 3 by default\n'
            '/pinlist - get history of pinned messages in pm\n'
            '/ban - ban a member\n'
            '/unban - unban a member\n'
            '/chat_id - get chat id\n'
            '/user - get info about user, see more in /help\n'
            '/ke - check if bot is alive\n'
            '/time - get time in location or timezone, more in /help\n'
            '/weather - get time in location, more in /help\n'
            '/gramota - check info about a word\n'
            '/mask - find a word by mask, see more in /help\n'
            '/spell - check word or frase spelling\n'
            '/get_first_msg - see first message of user\n'
            '/run_changer - clean flood after hangbot\n'
            '/her - get her of the day\n'
            '/fwd_to_text - start handling msgs for messages-to-one\n'
            '/stop - stop handling messages\n'
            '/get_message - get message array\n'
            '/q - get sticker from a message\n'
            '/create_list - create a list\n'
            '/help - see help')


class Form(StatesGroup):
    help_define = State()
    fwded_msgs = State()
    add_to_list = State()
    add_markers_dict = State()
