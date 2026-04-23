from django.shortcuts import render, get_object_or_404
from .models import Course, Submission

def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.course

    total_questions = course.question_set.count()
    correct_answers = 0

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
