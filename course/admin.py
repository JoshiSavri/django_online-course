from django.contrib import admin
<<<<<<< HEAD
from .models import Course, Lesson, Question, Choice, Submission
from .models import Instructor, Learner
=======
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Inline for Choice inside Question
>>>>>>> fe9c786a3fb822416ddb4d3dfb3bf7ae22e5f485
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

<<<<<<< HEAD
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)

admin.site.register(Instructor)
admin.site.register(Learner)
=======
# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Register all models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)   # ✅ REQUIRED
admin.site.register(Learner)      # ✅ REQUIRED
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)   # ✅ REQUIRED
>>>>>>> fe9c786a3fb822416ddb4d3dfb3bf7ae22e5f485
