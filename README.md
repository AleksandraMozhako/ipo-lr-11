## Задания

### Задание 1: Настройка виртуального окружения и репозитория
- Создано виртуальное окружение для изоляции зависимостей проекта.
- Все необходимые пакеты перечислены в файле `requirements.txt`.
- Виртуальное окружение исключено из репозитория с помощью `.gitignore`.

### Задание 2: Парсинг цитат
- Программа парсит цитаты с сайта [Quotes to Scrape](https://quotes.toscrape.com/).
- Выводит данные в следующем формате:


Quote: “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”; Author: Albert Einstein;
Quote: “It is our choices, Harry, that show what we truly are, far more than our abilities.”; Author: J.K. Rowling;

### Задание 3: Сохранение данных в JSON
- Собранные цитаты сохраняются в файл `data.json` в структурированном виде:
```json
[
    {
        "quote": "The world as we have created it...",
        "author": "Albert Einstein"
    },
    ...
]
```
### Задание 4: Генерация HTML-страницы

На основе данных из data.json генерируется файл index.html с таблицей цитат.
Страница содержит:
- Заголовок "Собранные цитаты".
- Красивый фон (цвет, градиент или картинка).
- Оформленную таблицу с цитатами и авторами.
- Ссылку на оригинальный источник данных.


