# 📚 Book Collection API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.2-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.36-red?logo=sqlalchemy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

**Современный REST API для управления коллекцией книг**

[Русский](#-описание) | [English](#-description)

</div>

---

## 🇷🇺 Описание

REST API для управления коллекцией книг, построенный на FastAPI и SQLAlchemy. Поддерживает полный CRUD функционал, поиск, пагинацию и работу с кириллицей.

### ✨ Возможности

- 📖 **CRUD операции** - создание, чтение, обновление и удаление книг
- 🔍 **Умный поиск** - по названию, автору и году издания
- 📄 **Пагинация** - эффективная работа с большими коллекциями
- 🌍 **Поддержка Unicode** - работа с кириллицей и любыми языками
- 📝 **Автодокументация** - Swagger UI и ReDoc из коробки
- ✅ **Валидация данных** - на уровне Pydantic и SQLAlchemy
- 🚀 **Высокая производительность** - асинхронная обработка запросов
- 🗄️ **SQLite база данных** - не требует дополнительной настройки

### 🛠️ Технологии

- **FastAPI** - современный веб-фреймворк для создания API
- **SQLAlchemy 2.0** - мощная ORM для работы с базами данных
- **Pydantic v2** - валидация и сериализация данных
- **Uvicorn** - быстрый ASGI сервер
- **SQLite** - легковесная встроенная база данных

## 🚀 Быстрый старт

### Требования

- Python 3.13+
- pip

### Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/Anzherus/innowise_laboratory.git
cd book_api

# Создайте виртуальное окружение
python -m venv venv

# Активируйте виртуальное окружение
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установите зависимости
pip install -r requirements.txt
```

### Запуск

```bash
# Запустите сервер
python main.py
```

Сервер будет доступен по адресу: `http://127.0.0.1:8000`

### 📖 Документация API

После запуска откройте в браузере:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📚 Использование

### Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `GET` | `/health` | Проверка работоспособности API |
| `POST` | `/books/` | Создать новую книгу |
| `GET` | `/books/` | Получить список всех книг |
| `GET` | `/books/{id}` | Получить книгу по ID |
| `PUT` | `/books/{id}` | Обновить книгу |
| `DELETE` | `/books/{id}` | Удалить книгу |
| `GET` | `/books/search/` | Поиск книг по параметрам |

### Примеры использования

#### 1. Создание книги

```bash
curl -X POST "http://127.0.0.1:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Война и мир",
    "author": "Лев Толстой",
    "year": 1869
  }'
```

**Ответ:**
```json
{
  "id": 1,
  "title": "Война и мир",
  "author": "Лев Толстой",
  "year": 1869
}
```

#### 2. Получение всех книг

```bash
curl "http://127.0.0.1:8000/books/?page=1&page_size=10"
```

**Ответ:**
```json
{
  "books": [
    {
      "id": 1,
      "title": "Война и мир",
      "author": "Лев Толстой",
      "year": 1869
    }
  ],
  "total": 1,
  "page": 1,
  "page_size": 10,
  "total_pages": 1
}
```

#### 3. Поиск книг

```bash
curl "http://127.0.0.1:8000/books/search/?author=Толстой&year_from=1860&year_to=1880"
```

#### 4. Обновление книги

```bash
curl -X PUT "http://127.0.0.1:8000/books/1" \
  -H "Content-Type: application/json" \
  -d '{
    "year": 1870
  }'
```

#### 5. Удаление книги

```bash
curl -X DELETE "http://127.0.0.1:8000/books/1"
```

### Использование с Python

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Создать книгу
response = requests.post(
    f"{BASE_URL}/books/",
    json={
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }
)
book = response.json()
print(f"Создана книга с ID: {book['id']}")

# Получить все книги
response = requests.get(f"{BASE_URL}/books/")
books = response.json()
print(f"Всего книг: {books['total']}")

# Поиск книг
response = requests.get(
    f"{BASE_URL}/books/search/",
    params={"author": "Orwell"}
)
results = response.json()
print(f"Найдено книг: {results['total']}")

# Обновить книгу
response = requests.put(
    f"{BASE_URL}/books/{book['id']}",
    json={"year": 1950}
)

# Удалить книгу
response = requests.delete(f"{BASE_URL}/books/{book['id']}")
```

## 📁 Структура проекта

```
book_api/
├── main.py              # Главный файл приложения с роутами
├── models.py            # SQLAlchemy модели
├── schemas.py           # Pydantic схемы для валидации
├── database.py          # Настройка подключения к БД
├── crud.py              # CRUD операции
├── dependencies.py      # Зависимости FastAPI
├── requirements.txt     # Зависимости проекта
├── .gitignore          # Игнорируемые файлы
└── README.md           # Документация
```

## 🔧 Конфигурация

### База данных

По умолчанию используется SQLite с файлом `books.db`. Для изменения отредактируйте `database.py`:

```python
DATABASE_URL = "sqlite:///./books.db"
```

### Сервер

Настройки сервера в `main.py`:

```python
uvicorn.run(
    "main:app",
    host="127.0.0.1",  # Адрес
    port=8000,          # Порт
    reload=True,        # Автоперезагрузка при изменениях
    log_level="info"    # Уровень логирования
)
```


## 📊 Примеры запросов

### Создание нескольких книг

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

books = [
    {"title": "Война и мир", "author": "Лев Толстой", "year": 1869},
    {"title": "Анна Каренина", "author": "Лев Толстой", "year": 1877},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967},
]

for book in books:
    response = requests.post(f"{BASE_URL}/books/", json=book)
    print(f"✅ Добавлена: {book['title']}")
```

### Поиск и фильтрация

```python
# Найти все книги Толстого
response = requests.get(
    f"{BASE_URL}/books/search/",
    params={"author": "Толстой"}
)

# Найти книги 19 века
response = requests.get(
    f"{BASE_URL}/books/search/",
    params={"year_from": 1800, "year_to": 1899}
)

# Найти книги по названию
response = requests.get(
    f"{BASE_URL}/books/search/",
    params={"title": "Война"}
)
```


## 📝 Лицензия

Этот проект распространяется под лицензией MIT.

## 👤 Автор

Cлюсарь Станислав Юрьевич - [@Anzherus](https://github.com/Anzherus)

## 🙏 Благодарности

- [FastAPI](https://fastapi.tiangolo.com/) - за отличный фреймворк
- [SQLAlchemy](https://www.sqlalchemy.org/) - за мощную ORM
- [Pydantic](https://docs.pydantic.dev/) - за валидацию данных

---

<div align="center">

**⭐ Если проект был полезен, поставьте звезду! ⭐**

</div>

---

## 🇬🇧 Description

REST API for managing a book collection, built with FastAPI and SQLAlchemy. Supports full CRUD functionality, search, pagination, and Unicode support.

### ✨ Features

- 📖 **CRUD Operations** - create, read, update, and delete books
- 🔍 **Smart Search** - by title, author, and publication year
- 📄 **Pagination** - efficient handling of large collections
- 🌍 **Unicode Support** - works with Cyrillic and any languages
- 📝 **Auto Documentation** - Swagger UI and ReDoc out of the box
- ✅ **Data Validation** - at Pydantic and SQLAlchemy levels
- 🚀 **High Performance** - asynchronous request processing
- 🗄️ **SQLite Database** - no additional setup required

### 🛠️ Technologies

- **FastAPI** - modern web framework for building APIs
- **SQLAlchemy 2.0** - powerful ORM for database operations
- **Pydantic v2** - data validation and serialization
- **Uvicorn** - fast ASGI server
- **SQLite** - lightweight embedded database

## 🚀 Quick Start

### Requirements

- Python 3.13+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Anzherus/innowise_laboratory.git
cd book_api

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running

```bash
# Start the server
python main.py
```

Server will be available at: `http://127.0.0.1:8000`

### 📖 API Documentation

After starting, open in browser:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📚 Usage

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Check API health |
| `POST` | `/books/` | Create a new book |
| `GET` | `/books/` | Get list of all books |
| `GET` | `/books/{id}` | Get book by ID |
| `PUT` | `/books/{id}` | Update book |
| `DELETE` | `/books/{id}` | Delete book |
| `GET` | `/books/search/` | Search books by parameters |

### Usage Examples

#### 1. Create a Book

```bash
curl -X POST "http://127.0.0.1:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "War and Peace",
    "author": "Leo Tolstoy",
    "year": 1869
  }'
```

**Response:**
```json
{
  "id": 1,
  "title": "War and Peace",
  "author": "Leo Tolstoy",
  "year": 1869
}
```

#### 2. Get All Books

```bash
curl "http://127.0.0.1:8000/books/?page=1&page_size=10"
```

**Response:**
```json
{
  "books": [
    {
      "id": 1,
      "title": "War and Peace",
      "author": "Leo Tolstoy",
      "year": 1869
    }
  ],
  "total": 1,
  "page": 1,
  "page_size": 10,
  "total_pages": 1
}
```

#### 3. Search Books

```bash
curl "http://127.0.0.1:8000/books/search/?author=Tolstoy&year_from=1860&year_to=1880"
```

#### 4. Update a Book

```bash
curl -X PUT "http://127.0.0.1:8000/books/1" \
  -H "Content-Type: application/json" \
  -d '{
    "year": 1870
  }'
```

#### 5. Delete a Book

```bash
curl -X DELETE "http://127.0.0.1:8000/books/1"
```

### Using with Python

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Create a book
response = requests.post(
    f"{BASE_URL}/books/",
    json={
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }
)
book = response.json()
print(f"Created book with ID: {book['id']}")

# Get all books
response = requests.get(f"{BASE_URL}/books/")
books = response.json()
print(f"Total books: {books['total']}")

# Search books
response = requests.get(
    f"{BASE_URL}/books/search/",
    params={"author": "Orwell"}
)
results = response.json()
print(f"Found books: {results['total']}")

# Update book
response = requests.put(
    f"{BASE_URL}/books/{book['id']}",
    json={"year": 1950}
)

# Delete book
response = requests.delete(f"{BASE_URL}/books/{book['id']}")
```

## 📁 Project Structure

```
book_api/
├── main.py              # Main application file with routes
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas for validation
├── database.py          # Database connection setup
├── crud.py              # CRUD operations
├── dependencies.py      # FastAPI dependencies
├── requirements.txt     # Project dependencies
├── .gitignore          # Ignored files
└── README.md           # Documentation
```

## 🔧 Configuration

### Database

SQLite is used by default with `books.db` file. To change, edit `database.py`:

```python
DATABASE_URL = "sqlite:///./books.db"
```

### Server

Server settings in `main.py`:

```python
uvicorn.run(
    "main:app",
    host="127.0.0.1",  # Address
    port=8000,          # Port
    reload=True,        # Auto-reload on changes
    log_level="info"    # Logging level
)
```


## 📊 Request Examples

### Creating Multiple Books

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

books = [
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
    {"title": "Anna Karenina", "author": "Leo Tolstoy", "year": 1877},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866},
    {"title": "The Master and Margarita", "author": "Mikhail Bulgakov", "year": 1967},
]

for book in books:
    response = requests.post(f"{BASE_URL}/books/", json=book)
    print(f"✅ Added: {book['title']}")
```

### Search and Filtering

```python
# Find all books by Tolstoy
response = requests.get(
    f"{BASE_URL}/books/search/",
    params={"author": "Tolstoy"}
)

# Find 19th century books
response = requests.get(
    f"{BASE_URL}/books/search/",
    params={"year_from": 1800, "year_to": 1899}
)

# Find books by title
response = requests.get(
    f"{BASE_URL}/books/search/",
    params={"title": "War"}
)
```


## 📝 License

This project is licensed under the MIT License. 

## 👤 Author

Slyusar Stanislav Yurievich - [@Anzherus](https://github.com/Anzherus)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - for the excellent framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - for the powerful ORM
- [Pydantic](https://docs.pydantic.dev/) - for data validation

---

<div align="center">

**⭐ If this project was helpful, give it a star! ⭐**

</div>
