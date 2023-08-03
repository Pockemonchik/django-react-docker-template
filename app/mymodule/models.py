from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import localdate
from datetime import datetime, date




class Record(models.Model):
    """Класс для загруженных для транскрибации записей"""
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Имя")
    file = models.FileField(upload_to="files",blank=True, default='', verbose_name="Файл")
    time = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    
    class Status(models.TextChoices):
        send = "send", "Отправлено"
        process = "process", "Обрабатывается"
        ready = "ready", "Готово"
        error = "error", "Ошибка"

    status = models.CharField(max_length=50, choices=Status.choices,
                              default=Status.send, null=True, blank=True)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["-time"]
    
    def __str__(self):
        try:
            if self.name:
                return self.name
            else:
                return str(self.id)
        except:
            return str(self.id)
        



