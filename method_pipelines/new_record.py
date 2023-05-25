import telebot
from telebot import types
from database_collector import df_append


class NewRecordPipeline:
    def __init__(self, bot: telebot.TeleBot):
        self.cache = []
        self.bot = bot

    def __call__(self, message: types.Message):
        self.bot.send_message(message.chat.id, 'Оцени свое настроение по шкале от 1 до 5')
        self.bot.register_next_step_handler(message, self.__get_emoji)

    def __get_emoji(self, message: types.Message):
        if message.text not in ['1', '2', '3', '4', '5']:
            self.bot.send_message(message.chat.id, 'Введи цифру от 1 до 5')
            self.bot.register_next_step_handler(message, self.new_record)
        else:
            self.cache.append(message.text)
            self.bot.send_message(message.chat.id, 'Отправь эмодзи, которая описывает твое настроение сейчас')
            self.bot.register_next_step_handler(message, self.__get_description)

    def __get_description(self, message: types.Message):
        self.cache.append(message.text)
        self.bot.send_message(message.chat.id, 'Опиши, что сегодня повлияло на твое настроение')
        self.bot.register_next_step_handler(message, self.__finalize_pipeline)

    def __finalize_pipeline(self, message: types.Message):
        self.cache.append(message.text)
        self.bot.send_message(message.chat.id, 'Запись добавлена, спасибо')
        df_append(message.date, message.from_user.username, message.from_user.id, self.cache[0], self.cache[1],
                  self.cache[2])
        self.cache = []
