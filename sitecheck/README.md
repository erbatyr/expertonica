# Проект SiteCheck

## Установка

Клонируем репозитории:

```sh
git clone https://github.com/erbatyr/expertonica.git
```
```sh
cd sitecheck
```

Создаем виртуальное окружение и устанавливаем зависимости:

```sh
pip install virtualenvwrapper-win
```
```sh
mkvirtualenv new_env
```
```sh
workon new_env
```

```sh
(new_env) pip install -r requirements.txt
```

После того как `pip` закончить установки:
```sh
(new_env) py manage.py runserver
```
И переходим по ссылке `http://127.0.0.1:8000/sitecheck/`.


## Навигация

На главной странице будут показаны список сайтов. Можно загрузить свой
список сайтов нажатием `Upload File` (файл должен быть `.xlsx` расширением). 
В таблице показывается `http_code`, `date`, `timeout` последней проверки сайта.  
Для обновления данных нажмите ссылку `check`.
В каждой странице будут показаны по 20 строчек. Также есть навигация
по страницам.

Базовая страница `api`: `http://localhost:8000/sitecheck/api/`

`URL api` списка сайтов: `http://localhost:8000/sitecheck/api/sites/`

`URL api` отдельного сайта: `http://localhost:8000/sitecheck/api/sites/?url=<url_сайта>/`
