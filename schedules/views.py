from django.shortcuts import render
from django.http import HttpResponse
from scms import models

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the scheduler")


def get_schedule(request, schedule_id):
    schedule = models.StudentCourseEnrollment.objects.filter('')
    return HttpResponse("TODO: Write this.")