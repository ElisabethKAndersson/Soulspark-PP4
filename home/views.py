from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
# from .forms import LeaveReview, Post
# Create your views here.


# Index page
def index(request):
    """ Index page """

    return render(request, 'home/index.html')
