from django.urls import path

from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView


app_name = 'deposite'


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("profile/", TransactionRepostView.as_view(), name="profile"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
]
