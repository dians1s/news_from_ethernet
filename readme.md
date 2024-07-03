# News From Ethernet
Веб-приложение для новостного сайта, собирающего информацию из других источников.


## Установка (Linux)
ВАЖНО: У вас должны быть установлены [зависимости проекта](https://github.com/dians1s/news_from_ethernet#зависимости)
1. Необходимо склонировать репозиторий

```git clone https://github.com/dians1s/news_from_ethernet.git```

2. Переход в директорию 'news_from_ethernet'

```cd news_from_ethernet```

3. Создание .env файла

Создайте .env файл в директории клонирования и внесите Ваш SECRET_KEY

```SECRET_KEY=...```

4. Установка зависимостей

```pip3 install -r requirements.txt```

5. Запуск скрипта сайта и парсера

```python3 ./manage.py runserver```
```python3 ./parser_rss.py```

## Поддержка
Если у вас возникли какие-либо проблемы или вопросы по использованию, создайте [обсуждение](https://github.com/dians1s/news_from_ethernet/issues/new/choose) в данном репозитории или напишите на электронную почту <danis11255@gmail.com>.

## Зависимости
Запускалось и разрабатывалось на интепретаторе Python версии 3.12.1 & PIP 24.0.0. Если вы заметили, что он данное ПО можно запустить на версии ниже, или он не работает на какой-либо версии, то напишите в [поддержку](https://github.com/dians1s/news_from_ethernet#поддержка)