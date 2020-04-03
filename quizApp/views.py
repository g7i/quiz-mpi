from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from accounts.models import Attempted
from .models import Quiz


@login_required(login_url='/accounts/')
def index(request):
    quizzes = list(Quiz.objects.filter(is_active=True).filter(subject=request.user.last_name).order_by('-created'))
    attempted = list(Attempted.objects.filter(user=request.user).values_list('quiz', flat=True))
    for quiz in Quiz.objects.filter(is_active=True).order_by('-created'):
        if quiz.id in attempted:
            quizzes.remove(quiz)
    context = {
        'quizzes': quizzes
    }
    return render(request, 'index.html', context)


@login_required(login_url='/accounts/')
def start(request, id):
    quiz = get_object_or_404(Quiz, pk=id)
    return render(request, 'quiz.html', {'quiz': quiz})
