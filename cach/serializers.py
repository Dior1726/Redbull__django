from rest_framework import serializers

from .models import Company, Bank, Transactions


class TransactionsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ("id", "title", "type", "sum")


class BankListSerializer(serializers.ModelSerializer):

    transactions = TransactionsListSerializer(many=True)

    class Meta:
        model = Bank
        fields = ("id", "title", "current_balance", "transactions")


class CompanyListSerializer(serializers.ModelSerializer):

    bank = BankListSerializer(many=True)

    class Meta:
        model = Company
        fields = ("id", "name", "bank")

