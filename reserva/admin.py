from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Status, Solicitacao, Perfil

# Register your models here.
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name = "perfil"

class UserAdmin(BaseUserAdmin):
    inlines = [PerfilInline]    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Solicitacao)
admin.site.register(Status)
