from django.contrib import admin

# Register your models here.
from .models import Review # 명시적 상대경로 표현

admin.site.register(Review)
