# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.12
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /flask-easy-feedback
# Скачиваем/обновляем необходимые библиотеки для проекта 
COPY requirement.txt /flask-easy-feedback
RUN pip3 install --upgrade pip -r requirements.txt
# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile, 
# в рабочую директорию контейнера
COPY . /backend
# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 5000