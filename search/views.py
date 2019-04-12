from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from issue_tracker.models import Bug, Content

# Create your views here.

def search_bugs(request):
    bugs = Bug.objects.filter(Q(title__icontains=request.GET['search']) | Q(bug_content__icontains=request.GET['search']))
    return render(request, "issue_tracker_bugs.html", {"bugs": bugs})
    
def search_content(request):
    contents = Content.objects.filter(Q(title__icontains=request.GET['search']) | Q(suggestion_content__icontains=request.GET['search']))
                                    
    return render(request, "issue_tracker_content.html", {"contents": contents})
    

## DROPDOWN FILTERING ON CONTENT PAGE

def filter_bugs(request):
    filter_var = request.POST.get('filter_dropdown', False)
    
    
    ## IF STATEMENT FOR FILTERING
    
    #filter by views
    if filter_var == "views":
        bugs = Bug.objects.all().order_by("-views")
    
    #filter by date
    elif filter_var == "newest":
        bugs = Bug.objects.all().order_by("-date_posted")
    
    #filter Backlog    
    elif filter_var == "a":
        bugs = Bug.objects.all().filter(status="a").order_by('-upvotes')
        
    #filter In Progress    
    elif filter_var == "b":
        bugs = Bug.objects.filter(status="b").order_by('-upvotes')
    
    #filter Completed     
    elif filter_var == "c":
        bugs = Bug.objects.filter(status="c").order_by('-upvotes')
    
    else:    
        bugs = Bug.objects.all().order_by('-upvotes')
        
    
    paginated_bugs = Paginator(bugs, 5)
    page = request.GET.get('page', 1)
    try:
        bugs = paginated_bugs.page(page)
    except PageNotAnInteger:
        bugs = paginated_bugs.page(1)
    except EmptyPage:
        bugs = paginated_bugs.page(paginated_bugs.num_pages)
        
    return render(request, "issue_tracker_bugs.html", {"bugs": bugs})
    
## DROPDOWN FILTERING ON CONTENTS PAGE

def filter_content(request):
    filter_var = request.POST.get('filter_dropdown', False)
    
    
    ## IF STATEMENT FOR FILTERING
    if filter_var == "views":
        contents = Content.objects.all().order_by("-views")
    
    elif filter_var == "newest":
        contents = Content.objects.all().order_by("-date_posted")
    
    #filter Backlog    
    elif filter_var == "a":
        contents = Content.objects.filter(status="a").order_by('-upvotes')
        
    #filter In Progress    
    elif filter_var == "b":
        contents = Content.objects.filter(status="b").order_by('-upvotes')
    
    #filter Completed     
    elif filter_var == "c":
        contents = Content.objects.filter(status="c").order_by('-upvotes')
    
    else:    
        contents = Content.objects.all().order_by('-upvotes')
        
    
    paginated_content = Paginator(contents, 5)
    page = request.GET.get('page', 1)
    try:
        contents = paginated_content.page(page)
    except PageNotAnInteger:
        contents = paginated_content.page(1)
    except EmptyPage:
        contents = paginated_content.page(paginated_content.num_pages)
        
    return render(request, "issue_tracker_content.html", {"contents": contents})
            
    
    
    
