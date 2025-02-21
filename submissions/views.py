from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Submission
from django.contrib import messages

# Create your views here.
def home(request):
    try:
        # Get filter parameters
        category = request.GET.get('category', '')
        status = request.GET.get('status', '')
        
        # Base queryset
        submissions = Submission.objects.all()
        
        # Apply filters
        if category:
            submissions = submissions.filter(category=category)
        if status == 'verified':
            submissions = submissions.filter(is_verified=True)
        elif status == 'reviewed':
            submissions = submissions.filter(is_reviewed=True, is_verified=False)
        elif status == 'pending':
            submissions = submissions.filter(is_reviewed=False, is_verified=False)

        context = {
            'submissions': submissions,
            'categories': Submission.CATEGORY_CHOICES,
            'selected_category': category,
            'selected_status': status,
        }
        return render(request, 'submissions/home.html', context)
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('home')

