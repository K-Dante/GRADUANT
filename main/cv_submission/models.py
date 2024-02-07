from django.db import models

class CV(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cv_file = models.FileField(upload_to='cv_submissions/')

    def __str__(self):
        return self.name