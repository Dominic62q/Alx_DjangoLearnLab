from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Book
from .models import Example
 

# ----------------------------
# Custom Forms for Admin
# ----------------------------
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

# ----------------------------
# Custom User Admin
# ----------------------------
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm       # Edit form
    add_form = CustomUserCreationForm # Creation form using custom manager

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# ----------------------------
# Book Admin
# ----------------------------
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

class ExampleAdmin(admin.ModelAdmin):
    list_display = ('example_field')
# ----------------------------
# Register models with admin.site.register
# ----------------------------
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Example, ExampleAdmin)