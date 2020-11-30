import os

from django.shortcuts import render
from django.views.generic.base import View


class MyResumeView(View):
    def get(self, request):
        return render(request, os.path.join('jobs', 'resume', 'resume.html'), {})
