from django.db import models


class Tip(models.Model):
    tip_percentage = models.IntegerField('Percentage', blank=False, null=False)

    tip = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.tip_percentage}'


class Discount(models.Model):
    discount_percentage = models.IntegerField('Percentage', blank=False, null=False)

    discount = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.discount_percentage}'

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'


#    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

class Type(models.Model):
    type_name = models.CharField('Name', max_length=50, blank=False, null=False)

    type = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.type_name}'

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'


class Employee(models.Model):
    employee_name = models.CharField('Name', max_length=50, blank=False, null=False)
    employee_password = models.CharField('Password', max_length=50, blank=False, null=False)
    employee_email = models.CharField('Email', max_length=50, blank=False, null=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)

    employee = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.user_name} - {self.user_email} - {self.user_password}'

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


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
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)

    table = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.table_name} - {self.creation_date} - {self.payment_date}'

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'


class Ticket(models.Model):
    total = models.IntegerField('Total', blank=False, null=False)
    tips = models.ForeignKey(Tip, on_delete=models.CASCADE, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)

    ticket = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.total} - {self.tips}'

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
