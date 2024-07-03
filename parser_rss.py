import feedparser
import asyncio
import httpx
import os
from news_from_ethernet.asgi import *
from main.models import News
from re import search
from bs4 import BeautifulSoup

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

sites = ["https://prian.ru/rss/news_ru.xml"]
#          "https://www.homesoverseas.ru/rss/"


async def summary_fixed(text):
    '''Форматируем и убираем теги из новости и убираем Photo by ..., если такое имеется'''
    temp = ''.join(BeautifulSoup(
        text, features="html.parser").findAll(string=True))
    try:
        temp = temp[:search(r'Photo', temp).start()]  # type: ignore
    finally:
        return temp


async def test_for_exception(head):
    '''Проверка на повторение'''
    test_for_exception = News.objects.filter(exception=head)
    return bool(test_for_exception)


async def send_news(title_parser_rss, sub_parser_rss, site_parser_rss, excp_parser_rss):
    '''Отправка новости в базу данных'''
    News.objects.create(title=title_parser_rss, subtitle=sub_parser_rss,
                        resource=site_parser_rss, person='parser_rss', exception=excp_parser_rss)
    return None


async def parser_rss(httpx_client, n_test_chars, send_message_func=None, loop=None):
    '''Парсинг новостных лент'''
    while True:
        try:
            response = []
            for i in sites:
                response.append(await httpx_client.get(i))
        except:
            await asyncio.sleep(10)
            continue

        feed = []
        for j in range(len(response)):
            feed.append(feedparser.parse(response[j].text))

        for k in range(len(feed)):
            for entry in feed[k].entries[::-1]:
                summary = f"{await summary_fixed(entry.get('fulltext'))}"
                title_from_pars = entry.get('title')
                # category = entry.get['category']

                head = summary[:n_test_chars].strip()

                if await test_for_exception(head):
                    continue

                if send_message_func is None:
                    print(title_from_pars, '\n', summary, '\n')

                else:
                    await send_message_func(title_from_pars, summary, sites[k], head)

                await asyncio.sleep(10)

        await asyncio.sleep(5)


if __name__ == "__main__":
    try:
        print("Процесс парсинга успешно запущен")
        n_test_chars = News._meta.get_field('exception').max_length
        httpx_client = httpx.AsyncClient()
        asyncio.run(parser_rss(httpx_client, n_test_chars,
                    send_message_func=send_news))
    except KeyboardInterrupt:
        print("Процесс парсера завершен")
