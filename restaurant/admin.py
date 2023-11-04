from django.contrib import admin
from restaurant.models import Category, Tip, Discount, Type, Employee, Product, Table, Ticket


# Register your models here.

class TipAdmin(admin.ModelAdmin):
    list_display = ('id', 'tip_percentage')
    search_fields = ('tip_percentage', 'id')
    list_filter = ('tip_percentage', 'id')


admin.site.register(Tip, TipAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name', 'id')
    list_filter = ('category_name', 'id')


admin.site.register(Category, CategoryAdmin)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount_percentage')
    search_fields = ('discount_percentage', 'id')
    list_filter = ('discount_percentage', 'id')


admin.site.register(Discount, DiscountAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    search_fields = ('type_name', 'id')
    list_filter = ('type_name', 'id')


admin.site.register(Type, TypeAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_name', 'employee_password', 'employee_email', 'type')
    search_fields = ('employee_name', 'type', 'id')
    list_filter = ('employee_name', 'type', 'id')


admin.site.register(Employee, EmployeeAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price')
    search_fields = ('product_name', 'id')
    list_filter = ('product_name', 'id')


admin.site.register(Product, ProductAdmin)


class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_name', 'creation_date', 'employee', 'total')
    search_fields = ('table_name', 'id')
    list_filter = ('table_name', 'id')


admin.site.register(Table, TableAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'tips', 'table', 'discount')
    search_fields = ('id', 'table')
    list_filter = ('id', 'table')


admin.site.register(Ticket, TicketAdmin)