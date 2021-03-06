from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Feedback
from rest_framework import viewsets
from .serializers import FeedbackSerializer
from django import forms
from django.db.models import Max

# Create your views here.
def index(request):
    if request.method == 'POST':
        item = Feedback.objects.get(id = id)
        item.state = False
        item.save()
        print(item.state)
    return render(request, "view/index.html",{'feedbacks': Feedback.objects.all()})

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "view/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "view/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "view/register.html", {
                "message": "Passwords must match."
            })
        #Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "view/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "view/register.html")

@login_required(login_url = '/login')
def create_feedback(request):
    if request.method == "POST":
        title= request.POST['title']
        description = request.POST['description']
        image = request.POST['image']
        category = request.POST['category']
        f=Feedback(title=title, description =description,image= image,category=category,creator = request.user)
        f.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "view/create.html" )

class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        queryset = Feedback.objects.all()
        return queryset