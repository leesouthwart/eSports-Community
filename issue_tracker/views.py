from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Bug, Content
from .forms import BugForm, BugCommentForm, ContentSuggestionForm, ContentCommentForm
import stripe
# Create your views here.


    
#page for bug reports on the issue tracker
def issue_tracker_bugs(request):
    filter_var = 'none'
    bug_list = Bug.objects.all().order_by('-upvotes')
    paginated_bugs = Paginator(bug_list, 5)
    page = request.GET.get('page', 1)
    try:
        bugs = paginated_bugs.page(page)
    except PageNotAnInteger:
        bugs = paginated_bugs.page(1)
    except EmptyPage:
        bugs = paginated_bugs.page(paginated_bugs.num_pages)
        
    return render(request, 'issue_tracker_bugs.html', {"bugs": bugs, "filter_var": filter_var})

# return a single bug page based on the PK
def single_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
   
    
    bug.views += 1
    bug.save()
    #comments ordering and pagination
    comments_list = bug.bug_comments.all().order_by("created_date")
    
    paginated_comments = Paginator(comments_list, 5)
    page = request.GET.get('page', 1)
    
    try:
        comments = paginated_comments.page(page)
    except PageNotAnInteger:
        comments = paginated_comments.page(1)
    except EmptyPage:
        comments = paginated_comments.page(paginated_comments.num_pages)
    
    
    ## adding comment form
    if request.method == "POST":
        form = BugCommentForm(request.POST)
        if form.is_valid():
            bug_comments = form.save(commit=False)
            bug_comments.post_id = pk
            bug_comments.author = request.user
            bug_comments.save()
            
            return HttpResponseRedirect(request.path_info, {'bug': bug, "form": form, "comments": comments})
    else:
        form = BugCommentForm
        
        
    return render(request, 'single_bug.html', {'bug': bug, "form": form, "comments": comments})

#delete bug post view
def delete_bug(request,pk):
    bug = get_object_or_404(Bug, pk=pk)
    Bug.objects.filter(id=pk).delete()
    return redirect('issue_tracker_bugs')
    


# create a bug or edit a bug view. If the pk is None, new bug will be created
@login_required
def create_or_edit_bug(request, pk=None): #pk defaulted to None
    
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    
    logged_in_user = request.user.username
    ## needs to be string to be able to compare to logged_in_user
    bug_user = str(bug.author) if pk else None
    
    # check to stop people forcing the url and editing other peoples posts
    if bug_user:
        if logged_in_user == bug_user or request.user.is_superuser:
        
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
        else:
            return redirect(issue_tracker_bugs)
        
    return render(request, 'new_bug.html', {'BugForm': form, 'bug': bug})
    

## BUG VOTES

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
    filter_var = "none"
    content_list = Content.objects.all().order_by('-upvotes')
    paginated_content = Paginator(content_list, 5)
    page = request.GET.get('page', 1)
    try:
        contents = paginated_content.page(page)
    except PageNotAnInteger:
        contents = paginated_content.page(1)
    except EmptyPage:
        contents = paginated_content.page(paginated_content.num_pages)
    
    return render(request, 'issue_tracker_content.html', {"contents": contents, "filter_var": filter_var})



# return a single content suggestion page based on the PK
def single_content(request, pk):
    
    key = settings.STRIPE_PUBLISHABLE
    
    content = get_object_or_404(Content, pk=pk)
    content.views += 1
    content.save()
    
    #comments ordering and pagination
    comments_li = content.content_comments.all().order_by("created_date")
    
    paginated_comments = Paginator(comments_li, 5)
    page = request.GET.get('page', 1)
    
    try:
        comments = paginated_comments.page(page)
    except PageNotAnInteger:
        comments = paginated_comments.page(1)
    except EmptyPage:
        comments = paginated_comments.page(paginated_comments.num_pages)
   
    
    ## adding comment form
    if request.method == "POST":
        form = ContentCommentForm(request.POST)
        if form.is_valid():
            content_comments = form.save(commit=False)
            content_comments.post_id = pk
            content_comments.author = request.user
            content_comments.save()
            
            return HttpResponseRedirect(request.path_info, {'content': content, "form": form, "comments": comments, "key": key})
    else:
        form = ContentCommentForm
            
    return render(request, 'single_content.html', {'content': content, "form": form, "comments": comments, "key": key})


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
    
    logged_in_user = request.user.username
    #needs to be string to be able to compare with logged_in_user
    content_user = str(content.author) if pk else None
    
    # check to stop people forcing the url and editing other peoples posts
    
    if logged_in_user == content_user or request.user.is_superuser:
        
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
    else:
        return redirect(issue_tracker_content)
        
    return render(request, 'new_content.html', {'ContentSuggestionForm': form, 'content': content})


#add upvote onto content suggestion    
def upvote_content(request, pk):
    
    content = get_object_or_404(Content, pk=pk)
    
    
    ## STRIPE LOGIC FOR TAKING PAYMENTS
    
    stripe.api_key = settings.STRIPE_SECRET
    
    if request.method == "POST":
        charge = stripe.Charge.create(
            amount=100,
            currency="GBP",
            description="Buy Upvote for ",
            source=request.POST['stripeToken']
            )
        
        content.upvotes += 1
        content.save()
        return redirect(single_content, content.pk)
        
def graphs_page(request):
    
    # Data to be passed in to google charts in charts.js
    bugs_backlog = Bug.objects.all().filter(status="a").count()
    bugs_progress = bugs = Bug.objects.filter(status="b").count()
    bugs_completed = Bug.objects.filter(status="c").count()
    
    contents_backlog = Content.objects.filter(status="a").count()
    contents_progress = Content.objects.filter(status="b").count()
    contents_completed = Content.objects.filter(status="c").count()
    
    context = {
        "bugs_backlog": bugs_backlog,
        "bugs_progress": bugs_progress,
        "bugs_completed": bugs_completed,
        "contents_backlog": contents_backlog,
        "contents_completed": contents_completed,
        "contents_progress": contents_progress
    }
    print(bugs_progress)
    
    return render(request, 'graphs_page.html', context)


    
    
