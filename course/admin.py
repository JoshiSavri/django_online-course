from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission
from .models import Instructor, Learner
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)

admin.site.register(Instructor)
admin.site.register(Learner)