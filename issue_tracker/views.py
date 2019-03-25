from django.shortcuts import render
from .models import Bug
# Create your views here.
def issue_tracker(request):
    
    bugs = Bug.objects.all()
    return render(request, 'issue_tracker.html', {"bugs": bugs})