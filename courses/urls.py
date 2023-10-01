from django.urls import path
from courses.views import home ,coursePage
from django.contrib import admin
from django.conf.urls.static import static
from e_learning_website.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('', home, name='home'),
    path('course/<str:slug>',coursePage,name='coursepage')
    #path(url,function,name )
    # <str:slug> is dynamic parameter 
]

urlpatterns += static( MEDIA_URL , document_root = MEDIA_ROOT) 