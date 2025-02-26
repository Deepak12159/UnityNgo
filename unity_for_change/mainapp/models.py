from django.db import models
from django.contrib.auth.models import AbstractUser

class OrphanKid(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OldAgeHome(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AccidentSupport(models.Model):
    victim_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.victim_name


class EducationSupport(models.Model):
    student_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=255)
    scholarship_needed = models.BooleanField(default=False)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name
class OrphanKid(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='orphan_images/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

# ye mere se fix nhi hua isiliye uda diya saale ko 😎
# class CustomUser(AbstractUser):
#     is_verified = models.BooleanField(default=False)
