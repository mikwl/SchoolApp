from django.db import models

from django.db import models


class School(models.Model):
    school_name = models.CharField(max_length=250, verbose_name='Название школы')
    school_location = models.CharField(max_length=250, verbose_name='Адрес школы')

    def __str__(self):
        return self.school_name


class Group(models.Model):
    group_name = models.CharField(max_length=250, verbose_name='Название / номер группы')
    group_facultet = models.CharField(max_length=250, verbose_name='Факультет')
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа')

    def __str__(self):
        return self.group_name


class Student(models.Model):
    student_first_name = models.CharField(max_length=250, verbose_name='Имя учащегося')
    student_last_name = models.CharField(max_length=250, verbose_name='Фамилия учащегося')
    student_age = models.IntegerField(verbose_name='Возраст учащегося')
    student_group = models.ForeignKey(Group, on_delete=models.CASCADE,verbose_name='Группа')

    def __str__(self):
        return self.student_last_name


# class Predmet(models.Model):
#     predmet_name = models.CharField(max_length=250, verbose_name='Название предмета')
#
#     def __str__(self):
#         return self.predmet_name



