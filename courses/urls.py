from django.urls import path
from courses.views import home ,coursePage ,SignupView , LoginView , signout, checkout, verifyPayment
from django.contrib import admin
from django.conf.urls.static import static
from e_learning_website.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('', home, name='home'),
    path('signup',SignupView.as_view(),name='signup'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',signout,name='logout'),
    path('course/<str:slug>',coursePage,name='coursepage'),
    path('check-out/<str:slug>',checkout,name='check-out'),
    path('verify_payment/', verifyPayment,name='verify_payment'),
    #path(url,function,name )
    # <str:slug> is dynamic parameter 
]

urlpatterns += static( MEDIA_URL , document_root = MEDIA_ROOT) 