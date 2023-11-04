from django.db import models


class Tip(models.Model):
    tip_percentage = models.IntegerField('Percentage', blank=False, null=False)

    tip = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.tip_percentage}'


class Category(models.Model):
    category_name = models.CharField('Name', max_length=50, blank=False, null=False)

    category = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.category_name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


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
        return f'{self.id} - {self.employee_name} - {self.employee_email} - {self.employee_password}'

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Product(models.Model):
    product_name = models.CharField('Name', max_length=50, blank=False, null=False)
    product_price = models.IntegerField('Price', blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    product = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.product_name} - {self.product_price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Table(models.Model):
    name_choices = (
        ('table_1', 'Table 1'),
        ('table_2', 'Table 2'),
        ('table_3', 'Table 3'),
    )
    table_name = models.CharField(
        'Name',
        max_length=50,
        choices=name_choices,
        blank=False,
        null=False
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ManyToManyField(Product)
    total = models.IntegerField(blank=True, null=True)

    table = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.table_name} - {self.creation_date} - {self.employee} - {self.total}'

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'

    def calculate_total(self):
        if self.product.all():
            total = 0
            for product in self.product.all():
                total += product.product_price
            self.total = total
        else:
            self.total = 0

    def save(self, *args, **kwargs):
        self.calculate_total()
        super().save(*args, **kwargs)


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

