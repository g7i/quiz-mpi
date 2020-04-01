from django.contrib import admin

from .models import Question, Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)
    search_fields = ('name', 'is_active')


admin.site.register(Question)
admin.site.register(Quiz, QuizAdmin)
