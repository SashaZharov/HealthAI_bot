from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class UserProfile:
    name: str
    age: int
    height: float
    weight: float
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
    @property
    def bmi(self) -> float:
        """Рассчитывает индекс массы тела."""
        return self.weight / ((self.height / 100) ** 2)
    
    def get_bmi_category(self) -> str:
        """Возвращает категорию ИМТ."""
        bmi = self.bmi
        if bmi < 18.5:
            return "недостаточный вес"
        elif bmi < 25:
            return "нормальный вес"
        elif bmi < 30:
            return "избыточный вес"
        else:
            return "ожирение"
    
    def to_dict(self) -> dict:
        """Конвертирует профиль в словарь."""
        return {
            'name': self.name,
            'age': self.age,
            'height': self.height,
            'weight': self.weight,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'UserProfile':
        """Создает профиль из словаря."""
        return cls(
            name=data['name'],
            age=data['age'],
            height=data['height'],
            weight=data['weight'],
            created_at=data.get('created_at', datetime.now())
        )