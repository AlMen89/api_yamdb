# API_YaMDb
### Описание
API позволяет делать запросы на получение, создание, обновление, удаление различных данных проекта YaMDb с различными уровнями доступа.

Проект YaMDb собирает отзывы (Review) пользователей (Users) на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка».

В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр (Genre) из списка предустановленных.

Анонимные пользователи могут только просматривать описания произведений, читать отзывы и комментарии.

Аутентифицированный пользователь (user) может оставлять к произведениям текстовые отзывы, комментировать отзывы других пользователей, редактировать и удалять свои данные, отзывы, комментарии и ставить произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. На одно произведение пользователь может оставить только один отзыв.

Модератор (moderator) имеет те же права, что и аутентифицированный пользователь, плюс право удалять и редактировать любые отзывы и комментарии

Администратор (admin), как и суперюзер, имеет полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям (user, moderator, admin), менять данные их аккаунтов и регистрировать новых пользователей.
### Технологии
Python 3.7.9
Django 2.2.16
### Запуск проекта в dev-режиме (команды для Windows)
- Клонируйте репозитоий (ссылка для протокола SSH):
```
git clone git@github.com:AlMen89/api_yamdb.git
```
- Перейдите в репозиторий в командной строке:
```
cd api_yamdb
```
- Установите виртуальное окружение:
```
python -m venv venv
```
- Активируйте виртуальное окружение
```
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```
- Для запуска сервера в папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
### Примеры запросов
(полная документация доступна после запуска сервера по адресу http://127.0.0.1:8000/redoc/)
- Получение кода подтверждения на переданный email (регистрация нового пользователя):
```
POST /api/v1/auth/signup/
```
- Получение JWT-токена в обмен на username и confirmation code:
```
POST /api/v1/auth/token/
```
- Получение списка всех категорий произведений:
```
GET /api/v1/categories/
```
- Добавление жанра произведения:
```
POST /api/v1/genres/
```
- Частичное обновление информации о произведении:
```
PATCH /api/v1/titles/<titles_id>/
```
- Удаление отзыва по id:
```
DELETE /api/v1/titles/<title_id>/reviews/<review_id>/
```
- Получение комментария к отзыву:
```
GET /api/v1/titles/<title_id>/reviews/<review_id>/comments/<comment_id>/
```
- Удаление пользователя по username:
```
DELETE /api/v1/users/username/
```
