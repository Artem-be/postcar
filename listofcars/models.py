from django.db import models
from django.conf import settings

class Car(models.Model):
    """
    Модель для хранения информации об автомобилях.
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    make = models.CharField('марка автомобиля', max_length=255)
    model = models.CharField('модель автомобиля', max_length=255)
    year = models.IntegerField('год выпуска')
    description = models.TextField('описание автомобиля')
    created_at = models.DateTimeField('дата и время создания записи', auto_now_add=True)
    updated_at = models.DateTimeField('дата и время последнего обновления записи', auto_now=True)

    def __str__(self):
        return f'{self.make}, {self.model}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Comment(models.Model):
    """
    Модель для хранения комментариев к записям.
    """
    content = models.TextField('Текст комментария')
    created_at = models.DateTimeField('дата и время создания комментария',auto_now_add=True)
    car = models.ForeignKey('Car',verbose_name='Публикация',on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f'{self.car}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

