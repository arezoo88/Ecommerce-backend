from django.contrib import admin
from apps.account.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class ProfileAdmin(admin.ModelAdmin):
    list_display=('full_name','gender','user_email')
    def user_email(self,obj):
        return obj.user.email

class UserAdmin(admin.ModelAdmin):
        list_display=('email',)

    
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)

    
