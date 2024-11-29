from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    author = models.CharField(max_length=200, verbose_name='نویسنده')
    content = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    covers = models.ImageField(upload_to='BookCovers/', blank=True, verbose_name='عکس جلد کتاب')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])