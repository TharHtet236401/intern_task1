from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .models import Submission
from django.contrib import messages
from .forms import SubmissionForm

# Create your views here.
def home(request):
    try:
        # Get filter parameters
        category = request.GET.get('category', '')
        status = request.GET.get('status', '')
        page = request.GET.get('page', 1)
        
        # Base queryset
        submissions = Submission.objects.all()
        
        if category:
            submissions = submissions.filter(category=category)

        if status == 'reviewed':
            submissions = submissions.filter(is_reviewed=True)
        elif status == 'pending':
            submissions = submissions.filter(is_reviewed=False)

        # Get counts for different states
        total_count = submissions.count()
        reviewed_count = submissions.filter(is_reviewed=True).count()
        pending_count = submissions.filter(is_reviewed=False).count()

        # Pagination
        paginator = Paginator(submissions, 10)  # Show 10 submissions per page
        page_obj = paginator.get_page(page)

        context = {
            'submissions': page_obj,
            'categories': Submission.CATEGORY_CHOICES,
            'selected_category': category,
            'selected_status': status,
            'count': total_count,
            'reviewed_count': reviewed_count,
            'pending_count': pending_count,
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
        new_status = request.POST.get('status') == 'true'
        submission.is_reviewed = new_status
        submission.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

