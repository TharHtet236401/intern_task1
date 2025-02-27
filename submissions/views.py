from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.db.models import Count
from .models import Submission
from django.contrib import messages
from .forms import SubmissionForm

def home(request):
    try:
        # Get filter parameters
        #this block is taking the query from the url 
        category = request.GET.get('category', '')
        status = request.GET.get('status', '')
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', '1')
        
        # Base queryset
        #this is the base queryset that is used to get all the submissions
        submissions = Submission.objects.all().order_by('-created_at')
        
        # Apply filters
        if search_query:
            #this is the filter for the search query
            submissions = submissions.filter(content__icontains=search_query)
            
        if category:
            submissions = submissions.filter(category=category)

        if status == 'reviewed':
            submissions = submissions.filter(is_reviewed=True)
        elif status == 'pending':
            submissions = submissions.filter(is_reviewed=False)

       # now you got the filterd submissions
        # Get filtered counts by category
        text_count = submissions.filter(category='TEXT').count()
        image_count = submissions.filter(category='IMAGE_URL').count()
        total_count = text_count + image_count

        # Pagination
        paginator = Paginator(submissions, 10)
        try:
            page_obj = paginator.page(page)
        except:
            page_obj = paginator.page(1)

        context = {
            'submissions': page_obj,
            'categories': Submission.CATEGORY_CHOICES,
            'selected_category': category,
            'selected_status': status,
            'search_query': search_query,
            'total_count': total_count,
            'text_count': text_count,
            'image_count': image_count,
        }
        # if the request is from the htmx, then render the partial content_section.html with the data extracted from database
        if request.headers.get('HX-Request'):
            return render(request, 'submissions/partials/content_section.html', context)
        return render(request, 'submissions/home.html', context)
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        context = {
            'submissions': [],
            'categories': Submission.CATEGORY_CHOICES,
            'selected_category': '',
            'selected_status': '',
            'total_count': 0,
            'text_count': 0,
            'image_count': 0,
        }
        if request.headers.get('HX-Request'):
            return render(request, 'submissions/partials/content_section.html', context)
        return render(request, 'submissions/home.html', context)

def create_submission_view(request):
    try:
        if request.method == 'POST':
            form = SubmissionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        form = SubmissionForm()
        return render(request, 'submissions/create-submission.html', {'form': form})
    except Exception as e:
        return render(request, 'submissions/create-submission.html', {'form': SubmissionForm()})

def update_status(request, submission_id):
    try:
        #reject the request if it is not from the htmx cause it will update only the status
        if not request.headers.get('HX-Request'):
            return HttpResponse("Bad Request", status=400)
            
        submission = get_object_or_404(Submission, id=submission_id)
        new_status = request.POST.get('status') == 'true'
        submission.is_reviewed = new_status
        submission.save()
        #render the partial status_cell.html with the updated submission
        return HttpResponse(
            render_to_string('submissions/partials/status_cell.html', 
            {'submission': submission})
        )
    except Exception as e:
        return HttpResponse(f"Error updating status: {str(e)}", status=400)

