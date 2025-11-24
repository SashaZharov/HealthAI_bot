from telegram import Update
from telegram.ext import ContextTypes
from storage.user_storage import user_storage

async def show_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Показывает профиль пользователя."""
    user_id = update.message.from_user.id
    profile = user_storage.get_profile(user_id)
    
    if profile:
        await update.message.reply_text(
            f'📋 Ваш профиль:\n'
            f'• Имя: {profile.name}\n'
            f'• Возраст: {profile.age} лет\n'
            f'• Рост: {profile.height} см\n'
            f'• Вес: {profile.weight} кг\n'
            f'• ИМТ: {profile.bmi:.1f} ({profile.get_bmi_category()})\n\n'
            f'Используйте /start чтобы обновить профиль'
        )
    else:
        await update.message.reply_text(
            'Профиль не найден. Используйте /start чтобы создать профиль.'
        )