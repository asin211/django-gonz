from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     name = models.CharField(max_length=50, null=True)
#     email = models.EmailField(unique=True, null=True)

#     avatar = models.ImageField(null=True, default="avatar.svg")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


class CreateCustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": 'form-control my-4', "placeholder": 'Username'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": 'form-control my-4', "placeholder": 'Email'}))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={"class": 'form-control my-4', "placeholder": 'Password'}))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={"class": 'form-control my-4', "placeholder": 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateField()
    # date = models.DateField(auto_now_add=True)

    # for showing name as a contact in admin ui (changing model object header)
    def __str__(self):
        return self.name
        # return self.name + ' -- ' + self.email


# need to fix and register
class Department(models.Model):
    name = models.CharField(max_length=100)
    # administrators, agents, managers  (create this groups)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]     # ascending order
        # ordering = ['- name', ]    # descending order


class Employee(models.Model):
    # DEPARTMENT = (
    #     ('Administrators', 'Administrators'),
    #     ('Managers', 'Managers'),
    #     ('Agents', 'Agents'),
    # )
    # department = models.CharField(max_length=50, choices=DEPARTMENT)

    # name = models.CharField(max_length=40, null=True)

    name = models.CharField(max_length=50,)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    # phone = models.IntegerField()
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    position = models.CharField(max_length=50)
    # department = models.ManyToManyField(Department)
    date_created = models.DateField(auto_now_add=True)
    
    # user = models.ForeignKey("auth.User", on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class TourData(models.Model):
    tourName = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.FloatField()
    employee = models.ForeignKey(Employee, null=True, on_delete= models.SET_NULL)

    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    date_created = models.DateField(auto_now_add=True)
    # thumbnail = models.ImageField(null=True, blank=True, upload_to="images/")
    thumbnail = models.ImageField(default="slider-1.jpg", null=True, blank=True)


    def __str__(self):
        return self.tourName

    class Meta:
        ordering = ['tourName', ]
