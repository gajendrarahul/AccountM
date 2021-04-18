from django.contrib import admin
from .models import IncomeCategory, Income
# Register your models here.


class IncomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'amount']
    list_filter = ['category']
    search_fields = ['title']
    ordering = ['date']

    fieldsets = (
        ('General Information', {'fields': ('title', 'slug', 'description')}),
        ('Salary', {'fields': ('amount',)}),
        ('File', {'fields': ('image',)})
    )


admin.site.register(IncomeCategory)
admin.site.register(Income, IncomeAdmin)
