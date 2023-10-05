from django.shortcuts import render
# from django.http import HttpResponse
from courses.models import Course

# Create your views here.
def home(request):
    # fetching courses data from database courses
    courses = Course.objects.all()
    print(courses)
# template_name is name of file to be rendered after executing this function
# context is data we need to provide to display in that same html that we are going to render
    return render(request,template_name="courses/home.html",context= {"courses":courses   })
# path name will not include templates and start with structure inside templates i.e, courses-> home.html