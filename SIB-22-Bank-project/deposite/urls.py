from django.urls import path

from .views import DepositeMoneyView, WithdrawMoneyView, DepositeRepostView


app_name = 'deposite'


urlpatterns = [
    path("deposite/", DepositeMoneyView.as_view(), name="deposite_money"),
    path("profile/", DepositeRepostView.as_view(), name="profile"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
]
