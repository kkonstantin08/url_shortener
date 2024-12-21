**Документация URL-сокращателя**

**Описание проекта**

Данный проект является веб-приложением для сокращения ссылок. Пользователь может ввести оригинальную URL-ссылку, получить короткую версию и воспользоваться ею для перенаправления на исходную страницу. Проект основан на Flask и использует SQLite для хранения данных.

**Функциональность**

1. Генерация коротких URL-ссылок.
2. Перенаправление по короткой ссылке на оригинальный URL.
3. Ведение статистики посещений (количество визитов).
4. Отображение списка всех сокращенных ссылок.

**Требования**

- Python 3.7 или выше.
- Flask.
- Flask-WTF.
- SQLite (PostgreSQL или MySQL также могут быть использованы).

**Установка зависимостей**

```bash
pip install flask flask-sqlalchemy flask-wtf
```

**Настройка проекта**

1. Скопируйте код в файл (e.g., `url_shortener.py`).
2. Создайте SQLite базу данных выполнив код:
   ```python
   with app.app_context():
       db.create_all()
   ```
3. Запустите сервер Flask:
   ```bash
   python url_shortener.py
   ```

**Поток работы**

1. Откройте домен или localhost:5004 в браузере.
2. Введите URL в форму на главной странице.
3. Получите сокращенную ссылку.
4. Используйте короткую ссылку для перехода на оригинальную URL.

**Безопасность**

1. Не храните `SECRET_KEY` в публичных репозиториях.
2. Регулярно обновляйте библиотеки.
3. Защитите базу данных от SQL-injection.

---

**URL Shortener Documentation**

**Project Description**

This project is a web application for shortening URLs. Users can input a long URL, receive a shortened version, and use it for redirection to the original webpage. The project is based on Flask and uses SQLite for data storage.

**Features**

1. Generate shortened URLs.
2. Redirect using shortened links to the original URL.
3. Track visit statistics (number of visits).
4. Display a list of all shortened URLs.

**Requirements**

- Python 3.7 or higher.
- Flask.
- Flask-WTF.
- SQLite (PostgreSQL or MySQL can also be used).

**Dependency Installation**

```bash
pip install flask flask-sqlalchemy flask-wtf
```

**Project Setup**

1. Copy the code into a file (e.g., `url_shortener.py`).
2. Create the SQLite database by executing:
   ```python
   with app.app_context():
       db.create_all()
   ```
3. Start the Flask server:
   ```bash
   python url_shortener.py
   ```

**Workflow**

1. Open the domain or localhost:5004 in a browser.
2. Input a URL into the form on the homepage.
3. Receive the shortened link.
4. Use the shortened link to navigate to the original URL.

**Security**

1. Do not store `SECRET_KEY` in public repositories.
2. Regularly update dependencies.
3. Protect the database from SQL injection attacks.

