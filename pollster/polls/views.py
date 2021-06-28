import datetime

from django.utils import timezone
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Poll, Question, Choice, Response

# Get questions and display them


def index(request):
    active_polls = Poll.objects.filter(end_date__gt=timezone.now())
    return render(request, 'polls/index.html', {'polls': active_polls})

# Show specific question and choices

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Question.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/detail.html', {'poll': poll})

def question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/question.html', {'question': question})

# Get question and display results


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        if question.question_type == 'short answer':
            Response(response_text=request.POST['text'], question=question).save()
        elif question.question_type == 'Multiple choice question':
            for choice in request.POST.getlist('choice'):
                selected_choice = question.choice_set.get(pk=choice)
                selected_choice.votes += 1
                selected_choice.save()
        else:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
            selected_choice.votes += 1
            selected_choice.save()
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
