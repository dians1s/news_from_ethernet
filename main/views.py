from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all().order_by('-id')[:20:-1]
    titles = []
    subtitles = []
    for i in news:
        titles.append(News.get_title(i))
        subtitles.append(News.get_subtitle(i))

    data = {'output': zip(titles, subtitles)}
    return render(request, 'index.html', data)
