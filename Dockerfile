# 1. Используем базовый образ Python
FROM python:3.10-slim

# 2. Определяем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Копируем в контейнер файл с зависимостями и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копируем остальной код (бота) в контейнер
COPY . /app/

# 5. Задаём команду запуска (запустится bot.py)
CMD ["python", "bot.py"]
