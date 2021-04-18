from django.contrib import admin
from .models import ExpensesCategory, Expenses
# Register your models here.


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'amount']
    list_filter = ['category']
    search_fields = ['title']
    ordering = ['date']

    fieldsets = (
        ('General Information', {'fields': ('title', 'slug', 'description')}),
        ('Billing Information', {'fields': ('amount',)}),
        ('File', {'fields': ('image',)})
    )


admin.site.register(ExpensesCategory)
admin.site.register(Expenses, ExpensesAdmin)
