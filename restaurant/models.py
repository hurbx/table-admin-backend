from django.db import models


class Discount(models.Model):
    discount_percentage = models.IntegerField('Percentage', blank=False, null=False)

    discount = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.discount_percentage}'

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'


class Type(models.Model):
    type_name = models.CharField('Name', max_length=50, blank=False, null=False)

    type = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.type_name}'

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'


class User(models.Model):
    user_name = models.CharField('Name', max_length=50, blank=False, null=False)
    user_password = models.CharField('Password', max_length=50, blank=False, null=False)
    user_email = models.CharField('Email', max_length=50, blank=False, null=False)

    user = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.user_name} - {self.user_email} - {self.user_password}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Product(models.Model):
    product_name = models.CharField('Name', max_length=50, blank=False, null=False)
    product_price = models.IntegerField('Price', blank=False, null=False)
    product_quantity = models.IntegerField('Quantity', blank=False, null=False)

    product = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.product_name} - {self.product_price} - {self.product_quantity}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Table(models.Model):
    table_name = models.CharField('Name', max_length=50, blank=False, null=False)
    creation_date = models.DateTimeField('Creation Date', auto_now_add=True)
    payment_date = models.DateTimeField('Payment Date', blank=True, null=True)

    table = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.table_name} - {self.creation_date} - {self.payment_date}'

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'


class Ticket(models.Model):
    total = models.IntegerField('Total', blank=False, null=False)
    tips = models.IntegerField('Tips', blank=False, null=False)

    ticket = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.total} - {self.tips}'

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
