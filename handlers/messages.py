from telegram import Update
from telegram.ext import ContextTypes
from services.openai_service import openai_service
from storage.user_storage import user_storage

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает сообщения пользователя после регистрации."""
    user_id = update.message.from_user.id
    
    if not user_storage.profile_exists(user_id):
        await update.message.reply_text(
            'Пожалуйста, сначала зарегистрируйтесь с помощью команды /start'
        )
        return
    
    user_query = update.message.text
    profile = user_storage.get_profile(user_id)
    
    await update.message.chat.send_action(action="typing")
    
    try:
        answer = openai_service.get_health_advice(profile.to_dict(), user_query)
        await update.message.reply_text(answer)
        
    except Exception as e:
        await update.message.reply_text(
            'Извините, произошла ошибка при обработке вашего запроса. '
            'Пожалуйста, попробуйте позже.'
        )