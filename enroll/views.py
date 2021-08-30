from django.shortcuts import render
from django.views.generic import View , FormView
from .forms import EnrollForm
from .models import ClassInfo
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


class EnrollView(FormView):

    def get(self, request):
        form = EnrollForm()
        context = {'f': form, 'c': 'active'}
        template = 'enroll/index.html'
        return render(request, template,context)
    def post(self, request):
        form = EnrollForm(request.POST)
        context = {'f': form, 'c': 'active'}
        if form.is_valid():
            data = form.cleaned_data
            request.session['name'] = data['name']

            instance = ClassInfo()
            f = EnrollForm(request.POST, instance=instance)

            f.save()
            return HttpResponseRedirect(reverse('enroll:thanks'))
        else:
            return render(request, 'enroll/index.html', context)
class EnrollView2(View):
    def get(self, request):
        context = {'enroll_active': 'active'}
        template = 'enroll/index2.html'
        return render(request, template, context)


def ThanksView(request):
    if request.session.get('name'):
        template_name= 'enroll/thanks.html'
        name = request.session['name']
        del request.session['name'] #delete session after used it
        return render(request, template_name , {'name': name})
    else:
        return HttpResponseRedirect(reverse('enroll:enroll'))
