# from django.db.models import *



# from typing import Any
from django.shortcuts import render, redirect 
from courses.models import Course , Video , UserCourse


from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.utils.decorators import method_decorator




def my_course(request):
    return render(request,template_name="courses/my_courses.html")




@method_decorator(login_required(login_url='/login'),name='dispatch')

class MyCourseList(ListView):
    template_name = 'course/my_courses.html'
    context_object_name = 'user_courses'

    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)





# from django.db import models

# class Course(models.Model):
#     name = models.CharField(max_length = 50 , null = False)
#     slug = models.CharField(max_length = 50 , null = False , unique = True)
#     description = models.CharField(max_length = 200 , null = True)
#     price = models.IntegerField(null=False)
#     discount = models.IntegerField(null=False , default = 0) 
#     active = models.BooleanField(default = False)
#     thumbnail = models.ImageField(upload_to = "files/thumbnail") 
#     date = models.DateTimeField(auto_now_add= True) 
#     resource = models.FileField(upload_to = "files/resource")
#     length = models.IntegerField(null=False)

#     def __str__(self):
#         return self.name


# class CourseProperty(models.Model):
#     description  = models.CharField(max_length = 100 , null = False)
#     course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)

#     class Meta : 
#         abstract = True


# class Tag(CourseProperty):
#     pass
    
# class Prerequisite(CourseProperty):
#     pass

# class Learning(CourseProperty):
#     pass

# from django.shortcuts import render , redirect
# from django.shortcuts import HttpResponse
# from courses.models import Course , Video, UserCourse

# from django.contrib.auth.decorators import login_required
# Create your views here.


#using decorator so that MyCourse page can only be excess by user who logged in 
@login_required(login_url="login")
def MyCourses(request):
    user = request.user
   
    user_courses = UserCourse.objects.filter(user = user)
    #getting all courses of user 
    context = {
        'user_courses':user_courses
    }


    return render(request = request , template_name='courses/my_courses.html',context=context)




def coursePage(request,slug):
    
    course  = Course.objects.get( slug = slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by('serial_number')

    if serial_number is None : 
        serial_number = 1

    video = Video.objects.get(serial_number= serial_number, course= course)
    
    if (video.is_preview is False):
        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user  , course = course)
            except:
                return redirect("check-out" , slug=course.slug)
    
        # if you are enroll in this course then you can watch every video!
    
    context = {
        "course" : course,
        "video" : video,
        "videos" : videos,
    }
    return render(request , template_name="courses/course_page.html",context = context) 