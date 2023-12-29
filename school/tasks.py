from datetime import timedelta
import datetime
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from users.models import User
from .models import Course

@shared_task
def send_mail_course_update(pk, model):
    '''
    Отправляет письмо об изменении курса на электронную почту клиента
    '''
    for user in model:
        email = user.user
        send_mail(
            subject=f'Обновление курса',
            message=f'Курс {Course.objects.get(pk=pk)} обновился.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )

@shared_task
def user_block_task():
    '''
    Блокирует пользователя, если он неактивен 30 дней
    '''
    users = User.objects.all()
    today = datetime.datetime.now()
    delta_time = today - timedelta(days=30)

    for user in users:
        if user.last_login:
            tm = str(user.last_login)[:-6]
            format = '%Y-%m-%d %H:%M:%S.%f'
            time = datetime.datetime.strptime(tm, format)
            if user.is_active and time < delta_time:
                user.is_active = False
                user.save()
