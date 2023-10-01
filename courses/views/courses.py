from django.shortcuts import render
from django.shortcuts import HttpResponse
from courses.models import Course

# Create your views here.
def coursePage(request,slug):
    course = Course.objects.get(slug = slug)
    # we get course object according to slug asked by user 
    # .objects.get() for single object return and .objects.filter() for multiple object return 
    context = { "course": course}
    return render(request,template_name="courses/course_page.html",context=context)
# path name will not include templates and start with structure inside templates i.e, courses-> home.html