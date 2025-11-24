import os
from dotenv import load_dotenv

load_dotenv()

# Настройки бота
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Состояния разговора
NAME, AGE, HEIGHT, WEIGHT = range(4)

# Настройки OpenAI
OPENAI_MODEL = "gpt-5-mini"
OPENAI_MAX_TOKENS = 1000

# Валидация данных
MIN_AGE = 1
MAX_AGE = 150
MIN_HEIGHT = 50
MAX_HEIGHT = 250
MIN_WEIGHT = 20
MAX_WEIGHT = 300