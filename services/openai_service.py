import logging
from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_MAX_TOKENS
from config.prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL
    
    def get_health_advice(self, user_data: dict, user_query: str) -> str:
        """Получает совет по здоровью от OpenAI."""
        try:
            from config.prompts import HEALTH_ASSISTANT_PROMPT
            
            prompt = HEALTH_ASSISTANT_PROMPT.format(
                name=user_data['name'],
                age=user_data['age'],
                height=user_data['height'],
                weight=user_data['weight'],
                user_query=user_query
            )
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                max_completion_tokens=OPENAI_MAX_TOKENS,
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"Ошибка при обращении к OpenAI: {e}")
            raise

# Глобальный экземпляр сервиса
openai_service = OpenAIService()