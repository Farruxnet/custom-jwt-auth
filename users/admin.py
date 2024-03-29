from django.contrib import admin
from . models import User, Token
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'name', 'phone_number')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parol mos kelmadi")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text=("<a href=\"../password/\">Foydalanuvchi parolini o'zgartirish!</a>."))
    class Meta:
        model = User
        fields = ('name', 'username', 'phone_number', 'is_active', 'is_admin')

    def clean_password(self):

        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('username', 'name', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'phone_number', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'name', 'phone_number',)
    ordering = ('id',)
    filter_horizontal = ()

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    readonly_fields = ('access', 'refresh')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
