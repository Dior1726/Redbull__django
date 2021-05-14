from django.db import models


class Company(models.Model):
    """Компании"""
    name = models.CharField("Комания", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Bank(models.Model):
    """Счеты"""
    title = models.CharField("Название", max_length=100)
    current_balance = models.PositiveIntegerField("Доступно",)
    company = models.ForeignKey(Company, verbose_name="Компания", on_delete=models.SET_NULL, null=True, related_name="bank")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счеты"


class Transactions(models.Model):
    title = models.CharField("Описание", max_length=100)
    type = models.CharField("Тип", max_length=50)
    sum = models.PositiveIntegerField("Сумма")
    bank = models.ForeignKey(Bank, verbose_name="Счет", on_delete=models.SET_NULL, null=True, related_name="transactions")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
