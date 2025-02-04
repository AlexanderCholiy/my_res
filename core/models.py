from django.db import models


class GeneralBlogModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано', default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        'Добавлено', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Обновлено', auto_now=True
    )

    class Meta:
        abstract = True
