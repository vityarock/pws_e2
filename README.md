# pws_e2
код для запуска локально.
Версия на heroku - https://protected-peak-81530.herokuapp.com/
Запуск:

    git clone https://github.com/vityarock/pws_e2
    python3 -m pip install -r requirements.txt
    в файле https://github.com/vityarock/pws_e2/blob/main/mail/settings.py указать или импортировать параметры:
    EMAIL_HOST_USER = 'username@yandex.ru'
    EMAIL_HOST_PASSWORD
    SECRET_KEY
    
    
    
    
    python manage.py runserver
