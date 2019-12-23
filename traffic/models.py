from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    departure = models.CharField(max_length = 50, null = True, blank = True, verbose_name="Пунк відправлення")
    arrival = models.CharField(max_length = 50, null = True, blank = True, verbose_name="Пунк прибуття")
    distance = models.FloatField(null = True, blank = True, verbose_name="Дистанція")
    content = models.TextField(null = True, blank = True, verbose_name="Додаткова інформація")
    published = models.DateTimeField(auto_now_add = True, db_index = True, verbose_name="Добвлено")
    phone_number = PhoneNumberField(null = False, verbose_name = "Номер телефона")
    name = models.CharField(max_length = 50,  verbose_name="Ім'я")

    class Meta:
        verbose_name_plural="Замовлення"
        verbose_name="Замовлення"
        ordering = ['-published']
