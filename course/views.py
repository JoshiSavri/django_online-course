from django.shortcuts import render, get_object_or_404
from .models import Course, Choice, Submission

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course/course_details.html', {'course': course})


def submit_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    selected_choices = request.POST.getlist('choice')
    choices = Choice.objects.filter(id__in=selected_choices)

    submission = Submission.objects.create(
        user=request.user,
        course=course
    )

    submission.choices.set(choices)

    return evaluate_exam(request, submission.id)


def evaluate_exam(request, submission_id):
    submission = Submission.objects.get(id=submission_id)

    total = 0
    correct = 0

    for question in submission.course.question_set.all():
        total += 1

        selected = submission.choices.filter(question=question)
        correct_choices = question.choice_set.filter(is_correct=True)

        if set(selected) == set(correct_choices):
            correct += 1

    score = (correct / total) * 100 if total > 0 else 0

    return render(request, 'course/exam_result.html', {
        'score': score,
        'total': total,
        'correct': correct
    })