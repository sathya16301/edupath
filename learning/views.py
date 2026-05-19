from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Subject, Quiz, Progress, QuizScore
import random


def home(request):

    query = request.GET.get("q")

    if query:
        subjects = Subject.objects.filter(name__icontains=query)
        return render(request, "search_results.html", {
            "query": query,
            "search_results": subjects
        })

    subjects = Subject.objects.all()

    core_subjects     = subjects.filter(category__icontains="core")
    theory_subjects   = subjects.filter(category__icontains="theory")
    allied_subjects   = subjects.filter(category__icontains="allied")
    emerging_subjects = subjects.filter(category__icontains="emerging")

    # User progress data for sidebar
    completed_ids      = []
    completed_subjects = []
    completed_count    = 0
    total_count        = subjects.count()
    in_progress_count  = 0

    if request.user.is_authenticated:
        completed_progress = Progress.objects.filter(
            user=request.user, completed=True
        ).select_related('subject')

        completed_subjects = [p.subject for p in completed_progress]
        completed_ids      = [s.id for s in completed_subjects]
        completed_count    = len(completed_ids)
        in_progress_count  = total_count - completed_count

    context = {
        "core_subjects":     core_subjects,
        "theory_subjects":   theory_subjects,
        "allied_subjects":   allied_subjects,
        "emerging_subjects": emerging_subjects,
        "completed_ids":      completed_ids,
        "completed_subjects": completed_subjects,
        "completed_count":    completed_count,
        "total_count":        total_count,
        "in_progress_count":  in_progress_count,
    }

    return render(request, "home.html", context)


def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, "subject_detail.html", {
        "subject": subject,
        "current_subject_id": subject.id
    })


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def quiz_view(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    quiz    = Quiz.objects.filter(subject=subject)

    if request.method == "POST":
        score = 0
        total = quiz.count()

        for q in quiz:
            answer = request.POST.get(str(q.id))

            # Map correct_answer (option1/option2/etc) to actual option text
            correct_map = {
                "1": q.option1,
                "2": q.option2,
                "3": q.option3,
                "4": q.option4,
                "option1": q.option1,
                "option2": q.option2,
                "option3": q.option3,
                "option4": q.option4,
            }
            correct_text = correct_map.get(q.correct_answer.lower().strip(), q.correct_answer)
            print(f"answer='{answer}' | correct_answer='{q.correct_answer}' | mapped='{correct_text}' | match={answer == correct_text}")

            if answer == correct_text:
                score += 1

        passed = total > 0 and score >= (total / 2)

        # Build results list for template highlighting
        results = []
        for q in quiz:
            user_answer = request.POST.get(str(q.id))
            correct_map = {
                "1": q.option1, "2": q.option2,
                "3": q.option3, "4": q.option4,
                "option1": q.option1, "option2": q.option2,
                "option3": q.option3, "option4": q.option4,
            }
            correct_text = correct_map.get(q.correct_answer.lower().strip(), q.correct_answer)
            results.append({
                "id": q.id,
                "question": q.question,
                "option1": q.option1,
                "option2": q.option2,
                "option3": q.option3,
                "option4": q.option4,
                "correct": correct_text,
                "user": user_answer,
                "opt1_class": "correct" if q.option1 == correct_text else ("wrong" if user_answer == q.option1 else ""),
                "opt2_class": "correct" if q.option2 == correct_text else ("wrong" if user_answer == q.option2 else ""),
                "opt3_class": "correct" if q.option3 == correct_text else ("wrong" if user_answer == q.option3 else ""),
                "opt4_class": "correct" if q.option4 == correct_text else ("wrong" if user_answer == q.option4 else ""),
            })

        # Save score if user is logged in
        if request.user.is_authenticated:
            QuizScore.objects.create(
                user=request.user,
                subject=subject,
                score=score,
                total=total
            )

            # Mark subject as completed if passed
            if passed:
                Progress.objects.update_or_create(
                    user=request.user,
                    subject=subject,
                    defaults={"completed": True}
                )

        return render(request, "quiz.html", {
            "quiz":    quiz,
            "subject": subject,
            "score":   score,
            "total":   total,
            "passed":  passed,
            "results": results,
        })

    quiz_list = list(quiz)
    random.shuffle(quiz_list)

    return render(request, "quiz.html", {
        "quiz":    quiz_list,
        "subject": subject,
        "score":   None,
    })