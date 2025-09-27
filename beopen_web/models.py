from django.db import models

class Post(models.Model):
    def __str__(self):
        return self.post_name

    post_name = models.CharField(max_length=255)
    post_title = models.CharField(max_length=255)
    content_file_path = models.CharField(max_length=255)
    visit_count = models.BigIntegerField(default=0)
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    tags = models.CharField(null=True, blank=True, max_length=1024)