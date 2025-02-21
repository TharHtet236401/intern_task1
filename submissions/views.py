from django.shortcuts import render
from django.http import HttpResponse
from .models import Submission

# Create your views here.
def get_submissions(request):
    try:
        selected_category = request.GET.get('category', '')
        if selected_category:
            submissions = Submission.objects.filter(category=selected_category)
        else:
            submissions = Submission.objects.all()
        
        categories = Submission.CATEGORY_CHOICES
        context = {
            'submissions': submissions,
            'categories': categories,
            'selected_category': selected_category
        }
        return render(request, 'submissions/home.html', context)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

