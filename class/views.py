from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from enroll.models import ClassInfo
# Create your views here.

class DisplayClass(View):
    def get(self, request):
        template_name = 'class/index.html'
        queries = ClassInfo.objects.filter(confirmed=True)
        queries = queries.values()

        context = {
            'b': 'active',
            'q': queries,
        }
        return render(request, template_name, context)