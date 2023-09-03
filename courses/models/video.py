from django.db import models
from courses.models import Course

class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE) # here CASCADE used for if course deleted than all tags releted to course is deleted
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=100, null=False)
    is_preview = models.BooleanField(default=False) # is_preview used to denote that preview of video is available or not (video is free or not), default preview is not available

    def __str__(self):
        return self.title