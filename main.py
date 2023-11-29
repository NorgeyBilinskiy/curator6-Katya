import telebot
bot = telebot.TeleBot('6717867395:AAH-zuj0RqOhSoRUUthcZ0fYMQHz2l_iqSk')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, {username}! Я - бот. Могу погадать тебе. Введи команду /guess', parse_mode='Markdown')
start_handler = CommandHandler('start', start)

updater.dispatcher.add_handler(start_handler)

def help_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я не могу предсказывать будущее, так как я всего лишь компьютерная программа.")

# создание обработчика команды /help
guess_handler = CommandHandler('guess', guess_command)

# добавление обработчика команды /help в диспетчер
updater.dispatcher.add_handler(guess_handler)

bot.infinity_polling()