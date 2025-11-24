from typing import Dict, Optional
from models.user_profile import UserProfile

class UserStorage:
    def __init__(self):
        self._profiles: Dict[int, UserProfile] = {}
    
    def save_profile(self, user_id: int, profile: UserProfile) -> None:
        """Сохраняет профиль пользователя."""
        self._profiles[user_id] = profile
    
    def get_profile(self, user_id: int) -> Optional[UserProfile]:
        """Возвращает профиль пользователя."""
        return self._profiles.get(user_id)
    
    def delete_profile(self, user_id: int) -> bool:
        """Удаляет профиль пользователя."""
        if user_id in self._profiles:
            del self._profiles[user_id]
            return True
        return False
    
    def profile_exists(self, user_id: int) -> bool:
        """Проверяет существование профиля."""
        return user_id in self._profiles

# Глобальный экземпляр хранилища
user_storage = UserStorage()