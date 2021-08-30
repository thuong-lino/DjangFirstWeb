from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, View, FormView


# from .models import Choice, Question


class IndexView(View):
    def get(self, request):
        template_name = 'homepage/index.html'
        context = {
            'home_active': 'active',  # active class for navigation bar

        }
        return render(request, template_name, context)

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'main/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'main/results.html'
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'main/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('main:results', args=(question.id,)))
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'main/results.html', {'question': question})
