import logging
from typing import Tuple, Optional
from models.user_profile import UserProfile
from storage.user_storage import user_storage

logger = logging.getLogger(__name__)

class ProfileService:
    @staticmethod
    def validate_age(age_text: str) -> Tuple[bool, Optional[int], Optional[str]]:
        """Валидирует возраст."""
        try:
            age = int(age_text)
            from config.settings import MIN_AGE, MAX_AGE
            if MIN_AGE <= age <= MAX_AGE:
                return True, age, None
            else:
                return False, None, f'Пожалуйста, введите возраст от {MIN_AGE} до {MAX_AGE}:'
        except ValueError:
            return False, None, 'Пожалуйста, введите возраст цифрами:'
    
    @staticmethod
    def validate_height(height_text: str) -> Tuple[bool, Optional[float], Optional[str]]:
        """Валидирует рост."""
        try:
            height = float(height_text)
            from config.settings import MIN_HEIGHT, MAX_HEIGHT
            if MIN_HEIGHT <= height <= MAX_HEIGHT:
                return True, height, None
            else:
                return False, None, f'Пожалуйста, введите рост от {MIN_HEIGHT} до {MAX_HEIGHT} см:'
        except ValueError:
            return False, None, 'Пожалуйста, введите рост цифрами:'
    
    @staticmethod
    def validate_weight(weight_text: str) -> Tuple[bool, Optional[float], Optional[str]]:
        """Валидирует вес."""
        try:
            weight = float(weight_text)
            from config.settings import MIN_WEIGHT, MAX_WEIGHT
            if MIN_WEIGHT <= weight <= MAX_WEIGHT:
                return True, weight, None
            else:
                return False, None, f'Пожалуйста, введите вес от {MIN_WEIGHT} до {MAX_WEIGHT} кг:'
        except ValueError:
            return False, None, 'Пожалуйста, введите вес цифрами:'
    
    @staticmethod
    def create_profile(user_id: int, name: str, age: int, height: float, weight: float) -> UserProfile:
        """Создает и сохраняет профиль пользователя."""
        profile = UserProfile(name=name, age=age, height=height, weight=weight)
        user_storage.save_profile(user_id, profile)
        logger.info(f"Создан профиль для пользователя {user_id}")
        return profile
    
    @staticmethod
    def get_profile_summary(profile: UserProfile) -> str:
        """Возвращает текстовое описание профиля."""
        return (
            f'🎉 Профиль создан!\n\n'
            f'📋 Ваши данные:\n'
            f'• Имя: {profile.name}\n'
            f'• Возраст: {profile.age} лет\n'
            f'• Рост: {profile.height} см\n'
            f'• Вес: {profile.weight} кг\n'
            f'• ИМТ: {profile.bmi:.1f} ({profile.get_bmi_category()})\n\n'
            f'Теперь вы можете задавать вопросы о здоровье, питании, тренировках и образе жизни!\n'
            f'Просто напишите ваш вопрос.'
        )