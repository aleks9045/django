from django.db import models


class Information(models.Model):
    name = models.CharField('Имя', max_length=20)
    name2 = models.CharField('Фамилия', max_length=20)
    age = models.SmallIntegerField('Возраст')
    sex = models.CharField('Пол', max_length=10)

    def __str__(self):
        return self.name
