from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.CharField(max_length = 500, blank = True)
    is_student = models.BooleanField(default = True)
    is_publisher = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user.username} - {'Publisher' if self.is_publisher else 'Student'}"
    
class Courses(models.Model):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    publisher = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'published_courses')
    video_url = models.URLField(help_text = "Paste the YouTube video link here")
    created_at = models.DateTimeField(auto_now_add = True)

    @property
    def replace_youtube_link(self):
        if not self.video_url:
            return ""

        # This handles standard watch?v= links, mobile youtu.be links, and shorts
        if 'watch?v=' in self.video_url:
            video_id = self.video_url.split('watch?v=')[1].split('&')[0]
        elif 'youtu.be/' in self.video_url:
            video_id = self.video_url.split('youtu.be/')[1].split('?')[0]
        elif 'shorts/' in self.video_url:
            video_id = self.video_url.split('shorts/')[1].split('?')[0]
        else:
            return self.video_url # Fallback

        return f"https://www.youtube.com/embed/{video_id}"
    
    def __str__(self):
        return self.title
    
