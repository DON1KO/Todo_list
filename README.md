# 📝 Todo List API

REST API для управления задачами, построенный на **Django** + **Django REST Framework**.

## Возможности

- ✅ CRUD операции с задачами (создать, читать, обновить, удалить)
- 🔐 Аутентификация — каждый пользователь видит только свои задачи
- 🔍 Фильтрация по статусу (`is_active`)
- 📄 Пагинация
- 🎨 Красивая админ-панель (Jazzmin)

## Технологии

- Python 3.10+
- Django 5.2
- Django REST Framework
- PostgreSQL
- django-filter
- django-environ

## Установка

```bash
# Клонировать репозиторий
git clone https://github.com/DON1KO/Todo_list.git
cd Todo_list

# Создать виртуальное окружение
python -m venv env
source env/bin/activate   # Linux/Mac
# env\Scripts\activate    # Windows

# Установить зависимости
pip install -r requirements.txt

# Настроить переменные окружения
cp .env.example .env
# Отредактируй .env — укажи свои данные БД

# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser

# Запустить сервер
python manage.py runserver
```

## API Endpoints

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/tasks/` | Список задач |
| POST | `/api/tasks/` | Создать задачу |
| GET | `/api/tasks/{id}/` | Детали задачи |
| PUT | `/api/tasks/{id}/` | Обновить задачу |
| DELETE | `/api/tasks/{id}/` | Удалить задачу |

### Фильтрация
```
GET /api/tasks/?is_active=true
```

### Пример запроса
```json
POST /api/tasks/
{
    "name": "Выучить Python",
    "description": "Пройти 14-дневный план обучения"
}
```

## Админ-панель

Доступна по адресу `/admin/` — красивый интерфейс Jazzmin.

## Автор

**DON1KO** — [GitHub](https://github.com/DON1KO)
