from django.contrib import admin

# Register your models here.

from .models import Student
from .models import Company
from .models import PasswordChangeLog
from .models import LoginHistory

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(PasswordChangeLog)
admin.site.register(LoginHistory)