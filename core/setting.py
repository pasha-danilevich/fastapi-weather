import os
from functools import lru_cache
from pathlib import Path
from typing import Any

from pydantic_settings import SettingsConfigDict, BaseSettings

BASE_PATH = Path(__file__).parent.parent


# Базовый класс для настроек
class BaseSettingsWithEnv(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_PATH, 'dev.env'),  # Указываем путь к файлу .env
        env_file_encoding='utf-8',  # Указываем кодировку файла
        extra='ignore',  # Игнорируем лишние переменные
    )

class DataBaseSettings(BaseSettingsWithEnv):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str


# Функция для получения настроек с кэшированием
@lru_cache()
def get_db_settings() -> DataBaseSettings:
    return DataBaseSettings()  # Возвращаем экземпляр настроек