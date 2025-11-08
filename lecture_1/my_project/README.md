# Hello World Color 🌈

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![Poetry](https://img.shields.io/badge/packaging-poetry-cyan)
![Tests](https://img.shields.io/badge/tests-19%20passed-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-88%25-green)

**A professional Python project demonstrating modern development practices with colorful terminal output**

</div>

## English Version

### Features

- **🎨 Colorful Terminal Output**: Cross-platform colored text using Colorama
- **🏗 Professional Structure**: Modern Python project layout with Poetry
- **🧪 Comprehensive Testing**: 19 tests with 88% code coverage
- **📦 Dependency Management**: Poetry for reliable dependency resolution
- **📚 Full Documentation**: Detailed README in English and Russian

### Installation

#### Prerequisites
- Python 3.13+
- Poetry (recommended) or pip

#### Using Poetry (Recommended)
```bash
# Clone the repository
git clone https:https://github.com/Anzherus/innowise_laboratory.git
cd lecture_1


# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

#### Using pip
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -e .
```

### Usage

#### Basic Usage
```bash
# Run the main application
poetry run python main.py

# Or use the installed script
poetry run hello-color
```

#### Expected Output
```
Hello World!                    # Red text on yellow background
Hello World in Green!           # Green text
Hello World in Bright Blue!     # Bright blue text
Hello World with Magenta text and Cyan background!  # Magenta on cyan
```

### Development

#### Running Tests
```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov

# Run tests verbosely
poetry run pytest -v
```

#### Adding Dependencies
```bash
# Add production dependency
poetry add package-name

# Add development dependency
poetry add --group dev package-name

### Testing Strategy

The project includes comprehensive tests:
- **Unit Tests**: Individual component testing
- **Integration Tests**: Component interaction testing
- **Parameterized Tests**: Multiple input combinations
- **Mock Testing**: External dependency isolation

```bash
# Test Results
19 passed, 88% coverage in 0.18s
```

## Русская Версия

### Особенности

- **🎨 Цветной вывод в терминал**: Кроссплатформенный цветной текст с использованием Colorama
- **🏗 Профессиональная структура**: Современная структура Python проекта с Poetry
- **🧪 Комплексное тестирование**: 19 тестов с 88% покрытием кода
- **📦 Управление зависимостями**: Poetry для надежного разрешения зависимостей
- **📚 Документация**: README на английском и русском языках

### Установка

#### Требования
- Python 3.13+
- Poetry (рекомендуется) или pip

#### Использование Poetry (Рекомендуется)
```bash
# Клонируйте репозиторий
git clone https:https://github.com/Anzherus/innowise_laboratory.git
cd lecture_1

# Установите зависимости
poetry install

# Активируйте виртуальное окружение
poetry shell
```

#### Использование pip
```bash
# Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

# Установите зависимости
pip install -e .
```

### Использование

#### Основное использование
```bash
# Запустите основное приложение
poetry run python main.py

# Или используйте установленный скрипт
poetry run hello-color
```

#### Ожидаемый вывод
```
Hello World!                    # Красный текст на желтом фоне
Hello World in Green!           # Зеленый текст
Hello World in Bright Blue!     # Яркий синий текст
Hello World with Magenta text and Cyan background!  # Пурпурный текст на голубом фоне
```

### Разработка

#### Запуск тестов
```bash
# Запустите все тесты
poetry run pytest

# Запустите тесты с покрытием
poetry run pytest --cov

# Запустите тесты с подробным выводом
poetry run pytest -v
```

#### Добавление зависимостей
```bash
# Добавьте production зависимость
poetry add package-name

# Добавьте development зависимость
poetry add --group dev package-name
```
### Стратегия тестирования

Проект включает комплексные тесты:
- **Юнит-тесты**: Тестирование отдельных компонентов
- **Интеграционные тесты**: Тестирование взаимодействия компонентов
- **Параметризованные тесты**: Множественные комбинации входных данных
- **Mock-тестирование**: Изоляция внешних зависимостей

```bash
# Результаты тестирования
19 пройдено, 88% покрытия за 0.18с
```

