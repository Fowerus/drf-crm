### Список команд для Django
1.0.12 =)

> ./manage.py makemigrations <br>
> ./manage.py migrate

### для разработки

- git clone https://gitlab.com/go-best/django-rest-api.git
- переходим в корень с файлом Pipfile <br>
- вводим следующее <br>

  > pipenv shell <br>
  > pipenv install <br>
  > ./restapi/manage.py runserver <br>

---

#### Запуск через bash (для файла настройки сборщика)

> q cd /home/gobest/django-rest-api/restapi <br>
> sudo supervisorctl stop gunicorn <br>
> pipenv run gunicorn restapi.wsgi:application --bind 0.0.0.0:8000 <br>
> sudo supervisorctl start gunicorn <br>

#### Алгоритмы сборки

- Остановить сервер
  > sudo supervisorctl stop gunicorn
  > cd /home/gobest/django-rest-api
- обновить изменения с репы
  > git pull https://$LOGIN_GIT:$PASSWORD_GIT@gitlab.com/go-best/django-rest-api
- Запустить сервер
  > sudo supervisorctl stop gunicorn
