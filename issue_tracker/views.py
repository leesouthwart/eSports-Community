from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Bug
from .forms import BugForm
# Create your views here.

#def issue_tracker_content(request):
 #   
  #  bug_list = Bug.objects.all().order_by('-upvotes')
   # paginated_bugs = Paginator(bug_list, 2)
    #page = request.GET.get('page', 1)
    #try:
     #   bugs = paginated_bugs.page(page)
    #except PageNotAnInteger:
    #    bugs = paginated_bugs.page(1)
    #except EmptyPage:
    #    bugs = paginated_bugs.page(paginated_bugs.num_pages)
        
    #return render(request, 'issue_tracker.html', {"bugs": bugs})
    
#page for bug reports on the issue tracker
def issue_tracker_bugs(request):
    
    bug_list = Bug.objects.all().order_by('-upvotes')
    paginated_bugs = Paginator(bug_list, 5)
    page = request.GET.get('page', 1)
    try:
        bugs = paginated_bugs.page(page)
    except PageNotAnInteger:
        bugs = paginated_bugs.page(1)
    except EmptyPage:
        bugs = paginated_bugs.page(paginated_bugs.num_pages)
        
    return render(request, 'issue_tracker_bugs.html', {"bugs": bugs})

# return a single bug page based on the PK
def single_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, 'single_bug.html', {'bug': bug})

#delete bug post view
def delete_bug(request,pk):
    bug = get_object_or_404(Bug, pk=pk)
    Bug.objects.filter(id=pk).delete()
    return redirect('issue_tracker_bugs')

# create a bug or edit a bug view. If the pk is None, new bug will be created
def create_or_edit_bug(request, pk=None): #pk defaulted to None
    
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            
            bug = form.save(commit=False)
            bug.author = request.user
            bug.date_posted = timezone.now()
            bug.save()
            return redirect(single_bug, bug.pk)
    else:
        form = BugForm(instance=bug)
        
    return render(request, 'new_bug.html', {'BugForm': form, 'bug': bug})
    
def upvote_bug(request, pk):
    
    bug = get_object_or_404(Bug, pk=pk)
    bug.upvotes += 1
    bug.save()
    return redirect(single_bug, bug.pk)
    
def downvote_bug(request, pk):
    
    bug  = get_object_or_404(Bug, pk=pk)
    bug.upvotes -= 1
    bug.save()
    return redirect(single_bug, bug.pk)
    