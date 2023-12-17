from django.db import models

from config import settings
from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    image = models.ImageField(upload_to='media/', verbose_name='картинка')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    price = models.FloatField(verbose_name='цена курса', default=10000)
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.name


class Lessons(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='курс', **NULLABLE)
    name = models.CharField(max_length=250, verbose_name='название')
    image = models.ImageField(upload_to='media/', verbose_name='картинка', null=True)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link = models.URLField(verbose_name='ссылка')
    url_materials = models.URLField(verbose_name='ссылка на материалы урока', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    price = models.FloatField(verbose_name='цена урока', default=1000)
    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.name

class Payments(models.Model):
    CASH = 'Наличные'
    TRANSFER = 'Перевод'

    CHOICES = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='пользователь', null=True)
    date_payment = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete= models.SET_NULL,verbose_name='оплаченый курс', null=True)
    lesson = models.ForeignKey(Lessons, on_delete= models.SET_NULL, verbose_name='оплаченый урок', null=True)
    payment_amount = models.FloatField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, choices=CHOICES, verbose_name='способ оплаты', blank=True)

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='пользователь', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='курс')

    def __str__(self):
        return f"{self.user}: {self.course}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'