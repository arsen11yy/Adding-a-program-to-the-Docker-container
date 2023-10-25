# Используем базовый образ Python
FROM python:3.8

# Устанавливаем зависимости
RUN pip install telebot

# Копируем исходный код в контейнер
COPY . /app

# Указываем рабочую директорию
WORKDIR /app

# Запускаем приложение
CMD ["python", "Version_1.py"]
