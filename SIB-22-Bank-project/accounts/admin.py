from django.contrib import admin

from .models import User, UserAddress, UserAccount, AccountType


admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(UserAccount)
admin.site.register(AccountType)
