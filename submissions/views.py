from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Submission
from django.contrib import messages

# Create your views here.
def home(request):
    try:
        # Get filter parameter
        category = request.GET.get('category', '')
        status = request.GET.get('status', '')
        

        #this was like selecting all submissions and
        ##and remove the submissions based on the each input the requestof like category and status
        # Base queryset
        submissions = Submission.objects.all()
        
        # if the query has the category , then we filter the submissions based on the category
        if category:
            submissions = submissions.filter(category=category)

        # if 
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

