from django.db import models

class Job(models.Model):
    title = models.TextField()
    summary = models.TextField()
    image = models.ImageField(upload_to='job-images/', blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.id, self.title)
