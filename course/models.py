from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
<<<<<<< HEAD
        return self.question_text
=======
        return self.question_text   # ✅ IMPORTANT
>>>>>>> fe9c786a3fb822416ddb4d3dfb3bf7ae22e5f485


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
<<<<<<< HEAD
        return f"{self.user.username} - {self.course.name}"
    

class Instructor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Learner(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
=======
        return f"{self.user.username} - {self.course.name}"   # ✅ IMPORTANT
>>>>>>> fe9c786a3fb822416ddb4d3dfb3bf7ae22e5f485
