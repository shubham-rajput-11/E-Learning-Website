from django.urls import path , include
from courses.views import    HomePageView ,verifyPayment ,  coursePage , SignupView , LoginView , signout , checkout ,MyCourses
from courses.views.courses import MyCourseList
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
# from e_learning_website.settings import MEDIA_ROOT, MEDIA_URL



urlpatterns = [
    # path('', home, name='home'),
    # path('signup',SignupView.as_view(),name='signup'),
    # path('login',LoginView.as_view(),name='login'),
    # path('logout',signout,name='logout'),
    # path('my-courses',MyCourses,name='my-courses'),
    path('', HomePageView.as_view() , name = 'home'),
    path('logout', signout , name = 'logout'),
    # path('my-courses', MyCourseList.as_view() , name = 'my-courses'),
    path('my-courses', MyCourses, name = 'my-courses'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('login', LoginView.as_view() , name = 'login'),
    path('course/<str:slug>',coursePage,name='coursepage'),
    path('check-out/<str:slug>',checkout,name='check-out'),
    path('verify_payment/', verifyPayment,name='verify_payment'),
    #path(url,function,name )
    # <str:slug> is dynamic parameter 
]

# urlpatterns += static( MEDIA_URL , document_root = MEDIA_ROOT) 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



