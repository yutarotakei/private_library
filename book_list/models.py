from django.db import models
from accounts.models import CustomUser


# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    author = models.CharField(verbose_name='著者名', max_length=40)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    ISBN = models.IntegerField(verbose_name='コード', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Book'

    def __str__(self):
        return self.title
