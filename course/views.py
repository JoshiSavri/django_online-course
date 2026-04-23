from django.shortcuts import render, get_object_or_404
from .models import Course, Submission

<<<<<<< HEAD
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course/course_details_bootstrap.html', {'course': course})
=======
def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.course
>>>>>>> fe9c786a3fb822416ddb4d3dfb3bf7ae22e5f485

    total_questions = course.question_set.count()
    correct_answers = 0

<<<<<<< HEAD
def submit_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    selected_choices = request.POST.getlist('choice')
    choices = Choice.objects.filter(id__in=selected_choices)

    submission = Submission.objects.create(
        user=request.user,
        course=course
    )

    submission.choices.set(choices)

    return show_exam_result(request, submission.id)


def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.course

    total_questions = course.question_set.count()
    correct_answers = 0

    for question in course.question_set.all():
        selected = submission.choices.filter(question=question)
        correct = question.choice_set.filter(is_correct=True)

        if set(selected) == set(correct):
            correct_answers += 1

    return render(request, 'course/exam_result.html', {
        'course': course,
        'score': correct_answers,
        'total': total_questions
    })
=======
    for question in course.question_set.all():
        selected_choices = submission.choices.filter(question=question)
        correct_choices = question.choice_set.filter(is_correct=True)

        if set(selected_choices) == set(correct_choices):
            correct_answers += 1

    score = correct_answers
    total = total_questions

    return render(request, 'course/exam_result.html', {
        'course': course,
        'submission': submission,
        'score': score,
        'total': total
    })
>>>>>>> fe9c786a3fb822416ddb4d3dfb3bf7ae22e5f485
