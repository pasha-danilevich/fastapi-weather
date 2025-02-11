# database/connection.py
from tortoise.contrib.fastapi import register_tortoise
from core.setting import get_db_settings


def init_tortoise(app):
    """
    Инициализация Tortoise ORM для FastAPI приложения.
    """
    # Получаем настройки базы данных
    db_settings = get_db_settings()

    # Формируем строку подключения к PostgreSQL
    db_url = f"postgres://{db_settings.DB_USER}:{db_settings.DB_PASS}@{db_settings.DB_HOST}:{db_settings.DB_PORT}/{db_settings.DB_NAME}"

    print(f"Подключение к базе данных: {db_url}")  # Для отладки

    # Регистрируем Tortoise ORM
    register_tortoise(
        app,
        db_url=db_url,  # Используем строку подключения из настроек
        modules={"models": ["models.user"]},  # Указываем путь к модели User
        generate_schemas=True,  # Автоматически создает таблицы в базе данных
        add_exception_handlers=True,  # Добавляет обработчики исключений Tortoise
    )