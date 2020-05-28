## Веб-приложение библиотеки книг  

Python, Django, sqlite.  

Проект сделан без виртуального окружение, поэтому просто скачивайте файлы и запускайте  
`python manage.py runserver`  

Сервер запускается на http://127.0.0.1:8000/  

Если без файла базы данных db.sqlite3, то сначала нужно сделать миграции и загрузить xml:  
`python manage.py makemigrations`  
`python manage.py migrate`  
`python manage.py loaddata data.xml`  

Используемые библиотеки: django, psycopg2, dj_database_url, Pillow.  

Функционал: 
- база данных книг с картинкой обложки 
- для книги можно указать имя друга, которому дали книгу на время 
- можно создать связи "автор, который вдохновил другого автора на написание произведения" 
- отдельные страницы для множественного добавления в базу новых книг и авторов 
- админка для редактирования, создания, удаления объектов (login admin, password 1)