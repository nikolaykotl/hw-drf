from rest_framework import serializers


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = 'http://youtube.com'
        if (str(dict(value).get(self.field))).find(url) == -1:
            raise serializers.ValidationError('Материалы урока должны быть на youtube.com')


