# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import timezone
import datetime
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.db import models



# ------text choices-----------


class Level(models.TextChoices):
    STUDENT = 'student', _('Sinh viên giỏi')
    TEACHER = 'teacher', _('Giáo viên đứng lớp')
    TEACHER2 = 'teacher2', _('Giáo viên tự do')
    LECTURER = 'lecturer', _('Giảng viên đại học')
    MASTER = 'master', _('Thạc sĩ')

class Sex(models.TextChoices):
    MALE = 'male', _('Nam')
    FEMALE = 'female', _('Nữ')
    BOTH = 'both', _('Cả hai')

# ------End text choices------------


# -------models-----------



class TuitorInfo(models.Model):
    tuitor_id = models.AutoField(primary_key=True)
    name = models.CharField('Họ và tên', max_length=100, blank=False)
    address = models.CharField('Địa chỉ', max_length=254, blank=False)
    year_birthday = models.CharField('Năm sinh', max_length=4, blank=False)
    sex = models.CharField('Giới tính', max_length=10, choices=Sex.choices, default=Sex.MALE)
    id_number = models.CharField('CMND/CCCD', max_length=12, blank=False)
    phone_number = models.CharField(max_length=12, blank=False)
    email = models.EmailField('Email', blank=False)
    level = models.CharField('Trình độ', max_length=10, choices=Level.choices, default=Level.LECTURER)
    work_place = models.CharField('Nơi công tác', max_length=200, blank=False,
                                  help_text='Nơi đang học hoặc nơi giảng dạy')
    major = models.CharField('Chuyên ngành', max_length=254, blank=False)
    describe = models.TextField('Mô tả', blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    # class YearInSchool(models.TextChoices):
    #     FRESHMAN = 'FR', _('Freshman')
    #     SOPHOMORE = 'SO', _('Sophomore')
    #     JUNIOR = 'JR', _('Junior')
    #     SENIOR = 'SR', _('Senior')
    #     GRADUATE = 'GR', _('Graduate')
    #
    # year_in_school = models.CharField(
    #     max_length=2,
    #     choices=YearInSchool.choices,
    #     default=YearInSchool.FRESHMAN,
    # )
    #
    # def is_upperclass(self):
    #     return self.year_in_school in {
    #         self.YearInSchool.JUNIOR,
    #         self.YearInSchool.SENIOR,
    #     }
    name= models.CharField('Tên người học' , blank = True,max_length=255)
    school = models.CharField('Trường', blank = True,max_length=255)

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
