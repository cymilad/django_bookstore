from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1, verbose_name='نام کاربری')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    author = models.CharField(max_length=200, verbose_name='نویسنده')
    content = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    covers = models.ImageField(upload_to='BookCovers/', blank=True, verbose_name='عکس جلد کتاب')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='نام کاربری')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='نام کتاب', related_name='comments')
    text = models.TextField(verbose_name='متن نظر')
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت نظر')
    is_active = models.BooleanField(default=True, verbose_name='غیرفعال یا فعال بودن نظر')

    def __str__(self):
        return f'{self.user} : {self.text}'