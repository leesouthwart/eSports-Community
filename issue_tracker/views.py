from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Bug, Content
from .forms import BugForm, ContentSuggestionForm
# Create your views here.

    
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
@login_required
def create_or_edit_bug(request, pk=None): #pk defaulted to None
    
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            
            bug = form.save(commit=False)
           
            # Set author to request.user if it is a new post
            # else, do not edit bug.author
            if not pk:
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
    if bug.upvotes >= 1:
    # check that upvotes is above 0. Dont let it go below 0.
        bug.upvotes -= 1
        bug.save()
        return redirect(single_bug, bug.pk)
    else: 
        return redirect(single_bug, bug.pk)
    

### CONTENT SUGGESTIONS VIEWS ### 


#page for content suggestions on the issue tracker
def issue_tracker_content(request):
    
    content_list = Content.objects.all().order_by('-upvotes')
    paginated_content = Paginator(content_list, 5)
    page = request.GET.get('page', 1)
    try:
        contents = paginated_content.page(page)
    except PageNotAnInteger:
        contents = paginated_content.page(1)
    except EmptyPage:
        contents = paginated_content.page(paginated_content.num_pages)
        
    return render(request, 'issue_tracker_content.html', {"contents": contents})



# return a single content suggestion page based on the PK
def single_content(request, pk):
    content = get_object_or_404(Content, pk=pk)
    content.views += 1
    content.save()
    return render(request, 'single_content.html', {'content': content})


#delete selected content suggestion post view
def delete_content(request,pk):
    content = get_object_or_404(Content, pk=pk)
    Content.objects.filter(id=pk).delete()
    return redirect('issue_tracker_content')



# create a content suggestion or edit a suggestion view. 
#If the pk is None, new content suggestion will be created
@login_required
def create_or_edit_content(request, pk=None): #pk defaulted to None
    
    content = get_object_or_404(Content, pk=pk) if pk else None
    if request.method == "POST":
        form = ContentSuggestionForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            
            content = form.save(commit=False)
            
            # Set content.author if its a new post, 
            # if not, dont edit the author
            if not pk:
                content.author = request.user
            
            content.date_posted = timezone.now()
            content.save()
            return redirect(single_content, content.pk)
    else:
        form = ContentSuggestionForm(instance=content)
        
    return render(request, 'new_content.html', {'ContentSuggestionForm': form, 'content': content})


#add upvote onto content suggestion    
def upvote_content(request, pk):
    
    content = get_object_or_404(Content, pk=pk)
    # ADD PAYMENT STUFF IN HERE:
        #IF PAYMENT SUCCESSFUL:
        
    content.upvotes += 1
    content.save()
    return redirect(single_content, content.pk)
   
        
#add downvote onto content suggestion
def downvote_content(request, pk):
   
    content = get_object_or_404(Content, pk=pk)
    
    if content.upvotes >= 1:
    # check that upvote number is above 0. Don't let it go below 0.
        content.upvotes -= 1
        content.save()
        return redirect(single_content, content.pk)
    
    else: 
        return redirect(single_content, content.pk)
