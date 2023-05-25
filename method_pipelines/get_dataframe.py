import telebot
from telebot import types
from database_collector import df_show


class GetRecordPipeline:
    def __init__(self, bot: telebot.TeleBot):
        self.cache = []
        self.bot = bot

    def __call__(self, message: types.Message):
        df_path = df_show(message.chat.id)
        df = open(df_path, 'rb')
        self.bot.send_document(message.chat.id, df)
