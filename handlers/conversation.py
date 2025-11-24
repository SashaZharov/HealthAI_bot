from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from config.settings import NAME, AGE, HEIGHT, WEIGHT
from services.profile_service import ProfileService
from storage.user_storage import user_storage

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Начинает разговор и запрашивает имя."""
    await update.message.reply_text(
        '👋 Добро пожаловать в Ассистент по Здоровью!\n\n'
        'Я помогу вам с рекомендациями по здоровью, питанию и образу жизни.\n\n'
        'Для начала давайте создадим ваш профиль.\n'
        'Как вас зовут?',
        reply_markup=ReplyKeyboardRemove()
    )
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Сохраняет имя и запрашивает возраст."""
    user_id = update.message.from_user.id
    name = update.message.text
    
    # Временно сохраняем имя в контексте
    context.user_data['name'] = name
    
    await update.message.reply_text(
        f'Приятно познакомиться, {name}! 🎉\n'
        'Сколько вам лет?'
    )
    return AGE

async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Сохраняет возраст и запрашивает рост."""
    user_id = update.message.from_user.id
    age_text = update.message.text
    
    is_valid, age, error_message = ProfileService.validate_age(age_text)
    
    if not is_valid:
        await update.message.reply_text(error_message)
        return AGE
    
    context.user_data['age'] = age
    
    await update.message.reply_text('Отлично! 📊\nКакой у вас рост (в см)?')
    return HEIGHT

async def get_height(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Сохраняет рост и запрашивает вес."""
    user_id = update.message.from_user.id
    height_text = update.message.text
    
    is_valid, height, error_message = ProfileService.validate_height(height_text)
    
    if not is_valid:
        await update.message.reply_text(error_message)
        return HEIGHT
    
    context.user_data['height'] = height
    
    await update.message.reply_text('Прекрасно! ⚖️\nКакой у вас вес (в кг)?')
    return WEIGHT

async def get_weight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Сохраняет вес и завершает регистрацию."""
    user_id = update.message.from_user.id
    weight_text = update.message.text
    
    is_valid, weight, error_message = ProfileService.validate_weight(weight_text)
    
    if not is_valid:
        await update.message.reply_text(error_message)
        return WEIGHT
    
    # Создаем и сохраняем профиль
    profile = ProfileService.create_profile(
        user_id=user_id,
        name=context.user_data['name'],
        age=context.user_data['age'],
        height=context.user_data['height'],
        weight=weight
    )
    
    # Отправляем сводку профиля
    summary = ProfileService.get_profile_summary(profile)
    await update.message.reply_text(summary)
    
    # Очищаем временные данные
    context.user_data.clear()
    
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Отменяет и завершает разговор."""
    context.user_data.clear()
    await update.message.reply_text(
        'Регистрация отменена. Используйте /start чтобы начать заново.',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END