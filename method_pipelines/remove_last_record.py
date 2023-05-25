import telebot
from telebot import types
from database_collector import df_delete


class RemoveLastRecordPipeline:
    def __init__(self, bot: telebot.TeleBot):
        self.bot = bot

    def _call__(self, message: types.Message):
        self.bot.send_message(message.chat.id, 'Для подтверждения удаления последней записи напиши слово "удалить"')
        self.bot.register_next_step_handler(message, self.__approve_removing)

    def __approve_removing(self, message: types.Message):
        if message.text == 'удалить':
            df_delete(message.from_user.id)
            self.bot.send_message(message.chat.id, 'Запись успешно удалена')
        else:
            self.bot.send_message(message.chat.id, 'Запись не была удалена')
