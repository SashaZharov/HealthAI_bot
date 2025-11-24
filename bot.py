import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler

from config.settings import TELEGRAM_TOKEN, NAME, AGE, HEIGHT, WEIGHT
from handlers.conversation import start, get_name, get_age, get_height, get_weight, cancel
from handlers.messages import handle_message
from handlers.commands import show_profile, show_help

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def setup_handlers(application: Application) -> None:
    """Настраивает обработчики бота."""
    
    # Conversation Handler для регистрации
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)],
            HEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_height)],
            WEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_weight)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчики
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler('help', show_help))
    application.add_handler(CommandHandler('profile', show_profile))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

def main() -> None:
    """Запускает бота."""
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    setup_handlers(application)
    
    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()