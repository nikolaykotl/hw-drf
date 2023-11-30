from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    image = models.ImageField(upload_to='HW-DRF/', verbose_name='картинка')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.name


class Lessons(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    image = models.ImageField(upload_to='HW-DRF/', verbose_name='картинка', null=True)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link = models.URLField(verbose_name='ссылка')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.name