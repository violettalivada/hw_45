from django.db import models


STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    date = models.DateField(auto_now_add=True, verbose_name='Дата выполнения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.description)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
