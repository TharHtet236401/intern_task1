from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Submission
from django.contrib import messages
from .forms import SubmissionForm

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

def create_submission_view(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submission created successfully')
            return redirect('home')
    else:
        form = SubmissionForm()
    return render(request, 'submissions/create-submission.html', {'form': form})

def update_status(request, submission_id):
    try:
        submission = get_object_or_404(Submission, id=submission_id)
        status_type = request.POST.get('status_type')
        new_status = request.POST.get('status') == 'true'

        if status_type == 'reviewed':
            submission.is_reviewed = new_status
        elif status_type == 'verified':
            submission.is_verified = new_status
        
        submission.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

