from django.db import models


STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default='Task', verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    date = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.description)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
