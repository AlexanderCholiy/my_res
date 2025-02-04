from django.db import models

from core.models import GeneralBlogModel


class Category(models.Model):
    title = models.CharField(
        'Название', max_length=128, unique=True
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Skill(GeneralBlogModel):
    title = models.CharField(
        'Название', max_length=128, unique=True
    )
    description = models.CharField(
        'Описание', max_length=1024, null=True, blank=True
    )
    skill_type = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='skills',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.title


class Description(models.Model):
    content = models.TextField('Содержание', unique=True)
    order = models.PositiveIntegerField(
        'Порядок отображения', default=0, blank=True
    )

    class Meta:
        verbose_name = 'описание'
        verbose_name_plural = 'Описание'
        ordering = ['order']

    def __str__(self):
        return self.content


class WorkExperience(GeneralBlogModel):
    company_name = models.CharField('Компания', max_length=256)
    position = models.CharField('Должность', max_length=128)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания', null=True, blank=True)
    description = models.CharField(
        'Описание', max_length=1024, null=True, blank=True
    )
    order = models.PositiveIntegerField(
        'Порядок отображения', default=0, blank=True
    )

    class Meta:
        verbose_name = 'опыт'
        verbose_name_plural = 'Опыт'
        ordering = ['order']

    def __str__(self):
        return f'{self.position} в {self.company_name}'


class Education(GeneralBlogModel):
    title = models.CharField('Название', max_length=255)
    degree = models.CharField('Степень', max_length=128, null=True, blank=True)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания', null=True, blank=True)
    description = models.CharField(
        'Описание', max_length=1024, null=True, blank=True
    )
    order = models.PositiveIntegerField(
        'Порядок отображения', default=0, blank=True
    )

    class Meta:
        verbose_name = 'образование'
        verbose_name_plural = 'Образование'
        ordering = ['order']

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    birth_date = models.DateField('Дата рождения')
    email = models.EmailField('Email', unique=True, null=True, blank=True)
    phone_number = models.CharField(
        'Телефон', max_length=15, null=True, blank=True, unique=True
    )
    address = models.CharField('Адрес', max_length=256, null=True, blank=True)
    telegram_link = models.URLField(
        'Telegram', null=True, blank=True, max_length=128, unique=True
    )
    github_link = models.URLField(
        'GitHub', null=True, blank=True, max_length=128, unique=True
    )

    class Meta:
        unique_together = ('first_name', 'last_name')
        verbose_name = 'личные данные'
        verbose_name_plural = 'Личные данные'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
