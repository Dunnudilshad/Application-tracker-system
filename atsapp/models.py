from django.db import models

# Create your models here.

class resume_score(models.Model):
    score = models.FloatField()
    resume = models.FileField(upload_to='resumes/')






