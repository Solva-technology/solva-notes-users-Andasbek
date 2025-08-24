# 📘 Note App

Учебное Django-приложение для работы с заметками, пользователями и категориями. Поддерживает регистрацию, авторизацию, восстановление пароля и разграничение прав доступа.

---

## 🚀 Возможности

* **Заметки (CRUD)**

  * Создание, редактирование, удаление заметок.
  * Привязка статуса и категорий.
  * Автоматическое сохранение автора (текущий пользователь).

* **Пользователи**

  * Регистрация, вход/выход, восстановление пароля.
  * Профиль с биографией и датой рождения (через модель `UserProfile`).
  * Список пользователей и их заметки.

* **Права доступа**

  * Редактировать и удалять заметку может только её автор или администратор.
  * В шаблонах кнопки «Редактировать» и «Удалить» показываются только автору/админу.

* **UI**

  * Bootstrap 5 для стилей.
  * Общий шаблон `base.html`, единый дизайн.

* **Docker**

  * Проект запускается в контейнерах с PostgreSQL.
  * Простая команда запуска `docker compose up`.

---

## 🛠️ Технологии

* Python 3.11
* Django 5.2
* PostgreSQL
* Docker / Docker Compose
* Bootstrap 5

---

## 📂 Структура проекта

```
note_app/
├── notebook_project/         # настройки Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── notes/                    # приложение "Заметки"
│   ├── models.py             # User, UserProfile, Note, Status, Category
│   ├── views.py              # CRUD для заметок и работа с пользователями
│   ├── forms.py              # формы для заметок
│   ├── urls.py
│   └── templates/notes/      # шаблоны для заметок
│       ├── base.html
│       ├── index.html
│       ├── note_detail.html
│       ├── note_form.html
│       ├── note_confirm_delete.html
│       ├── users_list.html
│       └── user_detail.html
├── users/                    # приложение "Пользователи"
│   ├── urls.py               # регистрация, логин, логаут, восстановление пароля
│   ├── views.py              # регистрация пользователя
│   └── templates/registration/
│       ├── login.html
│       ├── register.html
│       ├── logout.html
│       ├── password_reset_form.html
│       ├── password_reset_done.html
│       ├── password_reset_confirm.html
│       └── password_reset_complete.html
├── docker-compose.yml
├── Dockerfile
└── .env.example
```

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Andasbek/solva-notes-users-Andasbek.git
cd solva-notes-users-Andasbek
```

### 2. Настроить `.env`

Скопируй `.env.example` → `.env` и укажи данные для БД:

```
POSTGRES_DB=notes_db
POSTGRES_USER=notes_user
POSTGRES_PASSWORD=secret
```

### 3. Запуск через Docker

```bash
docker compose up --build
```

### 4. Применить миграции и создать суперпользователя

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

### 5. Открыть в браузере

* Главная: [http://localhost:8000/](http://localhost:8000/)
* Админка: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 🔑 Основные URL

### Заметки

* `/` — список заметок (главная)
* `/notes/<id>/` — детальная страница заметки
* `/notes/create/` — создать заметку
* `/notes/<id>/edit/` — редактировать
* `/notes/<id>/delete/` — удалить

### Пользователи

* `/users/` — список пользователей
* `/users/<id>/` — профиль пользователя

### Аутентификация

* `/auth/register/` — регистрация
* `/auth/login/` — вход
* `/auth/logout/` — выход
* `/auth/password_reset/` — восстановление пароля

---

## 👮 Права доступа

* Неавторизованный пользователь: может только просматривать заметки.
* Авторизованный: может создавать заметки, редактировать/удалять только свои.
* Администратор: может редактировать/удалять любые заметки.

---

## 📸 Скриншоты (добавь свои)

* Главная страница
* Просмотр заметки
* Регистрация
* Форма создания заметки

---

## 🧩 Дополнительно

* Для тестовых данных можно использовать `seed.py` (генерация пользователей, категорий и заметок).
* В админке доступны все модели: User, UserProfile, Note, Status, Category.
