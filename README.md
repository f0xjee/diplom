# Backend сервис для автоматизации закупок

Дипломный проект по профессии **Python-разработчик (расширенный курс)**.  
Backend-приложение реализовано на Django Rest Framework и предназначено для автоматизации закупок в розничной сети через REST API.

Сервис позволяет:
- регистрировать и авторизовывать пользователей;
- импортировать товары от поставщиков;
- получать каталог товаров;
- формировать корзину;
- оформлять заказы;
- получать уведомления по email.

---

## Стек технологий

- Python 3.10+
- Django 4+
- Django Rest Framework
- SQLite / PostgreSQL
- PyYAML
- Requests

---

## Установка и запуск проекта

Клонировать репозиторий:

```bash
git clone https://github.com/USERNAME/netology_pd_diplom.git
cd netology_pd_diplom


Создать виртуальное окружение и установить зависимости:

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Выполнить миграции:

python manage.py migrate


Создать суперпользователя:

python manage.py createsuperuser


Запустить сервер:

python manage.py runserver


Админка доступна по адресу:
http://127.0.0.1:8000/admin/

Импорт товаров

Импорт товаров выполняется через API:

POST /api/partner/update


В теле запроса передаётся ссылка на YAML-файл с товарами.

Пример файла:
https://github.com/netology-code/python-final-diplom/blob/master/data/shop1.yaml

Основные эндпоинты API
Регистрация
POST /api/register

Авторизация
POST /api/login

Список товаров
GET /api/products

Детали товара
GET /api/products/{id}

Корзина
GET /api/basket
POST /api/basket
DELETE /api/basket

Добавление адреса доставки
POST /api/contact

Подтверждение заказа
POST /api/order/confirm

Список заказов
GET /api/orders

Детали заказа
GET /api/orders/{id}

Сценарий работы пользователя

Пользователь регистрируется и авторизуется.

Получает список товаров.

Добавляет товары в корзину.

Добавляет адрес доставки.

Подтверждает заказ.

Получает email с подтверждением.

Может просмотреть список и детали своих заказов.

Email уведомления

В проекте реализованы email-уведомления:

при регистрации пользователя;

при подтверждении заказа.

Настройки email задаются в settings.py через переменные окружения.