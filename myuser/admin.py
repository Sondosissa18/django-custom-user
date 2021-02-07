# from django.contrib import admin

# # Register your models here.

# from django.contrib.auth.admin import UserAdmin
# from .models import MyUser

# admin.site.register(MyUser, UserAdmin)



from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = MyUser
    # list_display = ['email', 'username']

admin.site.register(MyUser, CustomUserAdmin)