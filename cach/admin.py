from django.contrib import admin
from .models import Company, Bank, Transactions


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)


class BankAdmin(admin.ModelAdmin):
    list_display = ("title", "current_balance", "company")
    list_display_links = ("title",)


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "sum", "bank",)
    list_display_links = ("title",)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Transactions, TransactionsAdmin)
