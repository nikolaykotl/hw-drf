#import pytz
import json

from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

#from config import settings

from school.models import Course, Lessons, Subscription

from users.models import User


class LessonsTestCase(APITestCase):
    def setUp(self):

        super().setUp()
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Тестовый курс')
        self.lesson = Lessons.objects.create(
            name='Тестовый урок',
            image=None,
            description='Тестовое описание',
            link='http://localhost:8000/4',
            url_materials='http://youtube.com/bbb',
            course=self.course,
            owner=self.user,
        )


    def test_lesson_list(self):
        """ Тест списка уроков """
        response = self.client.get(reverse('school:list_lesson'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'count': 1,
                          'next': None,
                          'previous': None,
                          'results': [
                              {'id': self.lesson.id,
                               'name': self.lesson.name,
                               'image': None,
                               'description': self.lesson.description,
                               'link': self.lesson.link,
                               'url_materials': self.lesson.url_materials,
                               'course': self.lesson.course.name,
                               'owner': self.lesson.owner_id,
                               }
                          ]
                          }
                         )

    def test_lesson_retrieve(self):
        """ Тест получения урока """

        response = self.client.get(reverse('school:detail_lesson', args=[self.lesson.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': self.lesson.id,
                          'name': self.lesson.name,
                          'image': None,
                          'description': self.lesson.description,
                          'link': self.lesson.link,
                          'url_materials': self.lesson.url_materials,
                          'course': self.lesson.course_id,
                          'owner': self.lesson.owner_id,
                          }
                         )

    def test_create_lesson(self):
        """ Проверка создания урока """
        data = {
            'name': 'Тест 2',
            'description': 'Тестовый 2',
            'link': 'http://test.com/4',
            'url_materials': 'http://youtube.com/qqqq',
            'course': self.lesson.course_id,
        }
        response = self.client.post(reverse('school:create_lesson'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lessons.objects.count(), 2)

    def test_lesson_create_link_validation(self):
        """ Проверка валидации ссылки на видео """
        data = {
            'name': 'Тест 3',
            'description': 'Тестовsq 3',
            'course': self.lesson.course_id,
            'link': 'https://www.test.com/',
            'url-materials': 'http://youtube.com/qqqq',
        }
        response = self.client.post(reverse('school:create_lesson'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'non_field_errors': ['Материалы урока должны быть на youtube.com']})

    def test_update_lesson(self):
        """ Проверка обновления урока """
        data = {
            'name': 'Тест изменение урока',
            'description': 'Тест изменения',
            'link': self.lesson.link,
            'course': self.lesson.course_id,
            'url_materials': self.lesson.url_materials,
        }
        response = self.client.put(reverse('school:update_lesson', args=[self.lesson.id]), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': self.lesson.id,
                          'name': 'Тест изменение урока',
                          'image': None,
                          'description': 'Тест изменения',
                          'link': self.lesson.link,
                          'url_materials': self.lesson.url_materials,
                          'course': self.lesson.course_id,
                          'owner': self.lesson.owner_id,
                          }
                         )

    def test_lesson_delete(self):
        """ Проверка удаления урока """
        response = self.client.delete(reverse('school:delete_lesson', args=[self.lesson.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lessons.objects.count(), 0)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Тестовый курс')
        self.lesson = Lessons.objects.create(
            name='Тестовый урок',
            description='Тестовое описание',
            course=self.course,
            owner=self.user,
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
           course=self.course,
        )

    def test_create_subscription(self):
        """ Тест создания подписки """
        data = {
            'user': self.subscription.user_id,
            'course': self.subscription.course_id,
        }
        response = self.client.post(reverse('school:create_subscription'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 2)


    def test_list_subscription(self):
        """ Тест списка подписок """
        response = self.client.get(reverse('school:list_subscription'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         [
                             {'id': self.subscription.id,
                              'user': self.subscription.user.email,
                              'course': self.subscription.course.name,
                              }
                         ])

    def test_subscription_delete(self):
        """ Тест удаления подписки """
        response = self.client.delete(reverse('school:delete_subscription', args=[self.subscription.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)
