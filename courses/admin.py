from django.contrib import admin
from courses.models import Course, Tag, Prerequisite, Learning, Video

# Register your models here.#

# TabularInline is used to show model in table formate
# StackedInline is used to show model in stack formate
class TagAdmin(admin.TabularInline): 
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.StackedInline):
    model = Video

# here we dosen't register models(Tag, Prerequisite, Learning, Video) so it dosen't make new table in admin panel
# ModelAdmin is for we can use are created model inliney in any another model
# ModelAdmin is used to inline models 
class CourseAdmin(admin.ModelAdmin): 
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]

admin.site.register(Course, CourseAdmin) 
# admin.site.register(Tag)
# admin.site.register(Prerequisite)
# admin.site.register(Learning)

admin.site.register(Video)