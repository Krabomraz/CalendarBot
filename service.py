import telebot
import yaml

from telebot import types
from method_pipelines.new_record import NewRecordPipeline
from method_pipelines.remove_last_record import RemoveLastRecordPipeline


menu_commands = {
    '/new_record': 'Добавить запись в таблицу',
    '/remove_last_record': 'Удалить последнюю свою запись из таблицы',
    '/get_dataframe': 'Получить таблицу'
}

if __name__ == "__main__":
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    token = config['telegram_bot_token']
    bot = telebot.TeleBot(token)
    bot.set_my_commands([
        types.BotCommand(k, v) for k, v in menu_commands.items()
    ])

    @bot.message_handler(commands=['start'])
    def start(message: types.Message):
        bot.send_message(message.chat.id,
                         "Это бот для сбора наблюдений эмоционального состояния. Привет!")


    @bot.message_handler(commands=['new_record'])
    def new_record(message: types.Message):
        pipeline = NewRecordPipeline(bot)
        pipeline.new_record(message)


    @bot.message_handler(commands=['remove_last_record'])
    def remove_last_record(message: types.Message):
        pipeline = RemoveLastRecordPipeline(bot)
        pipeline.remove_last_record(message)


    @bot.message_handler(commands=['get_dataframe'])
    def get_dataframe(message: types.Message):
        pass

    bot.polling(none_stop=True, interval=0)
