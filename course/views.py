from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Submission, Choice


# Show course and questions
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course/course_details_bootstrap.html', {'course': course})


# Submit exam
def submit_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        selected_choices = request.POST.getlist('choices')

        submission = Submission.objects.create(
            user=request.user,
            course=course
        )

        choices = Choice.objects.filter(id__in=selected_choices)
        submission.choices.set(choices)

        # ✅ IMPORTANT: redirect properly
        return redirect('show_exam_result', submission_id=submission.id)

    return redirect('course_detail', course_id=course.id)


# Show result
def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_choices = submission.choices.all()

    total_score = 0
    possible_score = 0

    # ✅ REQUIRED scoring logic
    for choice in selected_choices:
        if choice.is_correct:
            total_score += 1

    possible_score = submission.course.question_set.count()

    context = {
        'submission': submission,
        'score': total_score,
        'total': possible_score
    }

    return render(request, 'course/exam_result.html', context)
