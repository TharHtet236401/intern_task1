from django.shortcuts import render
from django.http import HttpResponse
from .models import Submission

# Create your views here.
def home(request):
    submissions = Submission.objects.all()
    return render(request, 'submissions/home.html', {'submissions': submissions})

