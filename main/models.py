from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, blank=False)
    subtitle = models.CharField(max_length=1024, blank=False)
    resource = models.CharField(max_length=32, default='None')
    date = models.DateField(auto_now_add=True)
    person = models.CharField(max_length=64, default='None')
    exception = models.CharField(max_length=64, blank=False, default="Test")

    def __str__(self):
        return f'{self.title}|||{self.subtitle}'

    def get_title(self):
        return f'{self.title}'

    def get_subtitle(self):
        return f'{self.subtitle}'
