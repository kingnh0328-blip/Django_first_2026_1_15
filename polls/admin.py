from django.contrib import admin
from .models import Question, Choice
import datetime
from django.utils import timezone

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("제목", {"fields": ["question_text"]}),
        ("날짜정보", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    
    @admin.display(
        boolean=True,
        ordering="pub_date", 
        description="Published recently?",
    )
    
    def was_published_recently(self, obj):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= obj.pub_date <= now
    

# 관리자에 등록
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

