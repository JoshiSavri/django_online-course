from django.shortcuts import render, get_object_or_404
from .models import Course, Choice, Submission

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course/course_details_bootstrap.html', {'course': course})


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