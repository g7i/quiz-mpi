from django.contrib import admin

from .models import Attempted


class AttemptedAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz_name', 'got',)
    search_fields = ('user__username', 'quiz__name', 'got')

    def quiz_name(self, instance):
        return instance.quiz.name

    def student(self, instance):
        return instance.user.username


admin.site.register(Attempted, AttemptedAdmin)
