from contextlib import nullcontext
from email import message
from email.message import EmailMessage
from django.shortcuts import render, HttpResponse, redirect
# added manually
from datetime import datetime
from home.models import Contact, CreateCustomUserForm, TourData, Department, Employee

from django.contrib import messages
# manually added users
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm

# login required method
from django.contrib.auth.decorators import login_required



# person = [
#     {
#     'name': 'Steve',
#     'age': 30
#     },
#     {
#         'name': 'Steve',
#         'age': 30
#     },
# ]

# Create your views here.


def home(request):
    # return HttpResponse('Home page')
    tours = TourData.objects.all()
    context = {'tours': tours}
    # print(request.user.id)
    # print(request.user.is_superuser)
    # messages.success(request, 'Test message for alert messages')
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'home/home.html', context)


@login_required(login_url='login')
def about(request):
    return render(request, 'home/about.html')
    

@login_required(login_url='login')
def contact(request):
    # write logic here to save in database
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        context = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        context.save()
        messages.success(request, ' Your message has been sent!')


    # context = {'person': person}
    return render(request, 'home/contact.html')


@login_required(login_url='login')
def tours(request):
    tours = TourData.objects.all()
    context = {'tours': tours}
    return render(request, 'home/tours.html', context)


@login_required(login_url='login')
def tourDetail(request, pk):
    tour = TourData.objects.get(id=pk)
    context = {'tour': tour}
    return render(request, 'home/tour-detail.html', context)


@login_required(login_url='login')
def agents(request):
    agents = Department.objects.get(name="Agent").employee_set.all()
    context = {'agents': agents}
    return render(request, 'home/agents.html', context)


@login_required(login_url='login')
def agentDetail(request, pk):
    agent =  Employee.objects.get(id=pk)
    context = {'agent': agent}
    return render(request, 'home/agent-detail.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            # for testing purposes
            # print(username, password)

            # check if user credentials are right
            user = authenticate(username=username, password=password)
            # user = authenticate(request, username=username, password=password)


            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/")
                # return redirect("home")
            else:
                # No backend authenticated the credentials
                messages.info(
                    request, 'Username or Password is incorrect!')   
    return render(request, 'home/login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')
    # return redirect('/')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
    # form = UserCreationForm()
        form = CreateCustomUserForm()
        if request.method == 'POST':
            # form = UserCreationForm(request.POST)
            form = CreateCustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Created Successfully for  ' + user)
                return redirect('login')
                # user = form.save(commit=False)
                # user.save()
                # login(request, user)
            #     return redirect('home')
            # else:
            #     messages.error(request, 'An error occurred during registration. Please make sure password is 8 character long')
            else:
                # No backend authenticated the credentials
                messages.info(
                    # request, 'Username or Password is incorrect!')
                    request, form.errors)
    context = {'form': form }
    return render(request, 'home/register.html', context)

    # return render(request, 'home/register.html')


@login_required(login_url='login')
def addTour(request):
    # write logic here to save in database
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        filename = request.POST.get('filename')
        context = TourData(tourName=name, price=price,
                          desc=desc, date_created=datetime.today(), thumbnail=filename)
        context.save()
        messages.success(request, ' Your Tour has been created!')

    return render(request, 'home/create-tour.html')


# def updateTour(request, pk):
#     tour = request.POST.get(id=pk)
#     if request.method == "POST":
#         tour.delete()
#     return redirect('tours')
