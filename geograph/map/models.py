from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'map_{}/{}'.format(instance, filename)

class PeopleOfVaak(models.Model):
  CHOICES = (
      ('1', 'Team'),
      ('2', 'Directors'),
  )
  category = models.CharField(max_length=255, choices=CHOICES)
  name = models.CharField(max_length=255)
  image = models.FileField(upload_to=user_directory_path, null=True, blank=True)
  designation = models.TextField()
 
class Demo(models.Model):
    subject_choice = (
      ('1', 'python'),
      ('2', 'django'),
  )
    budget_choice = (
      ('1', '5000'),
      ('2', '10000'),
  )
    Name = models.CharField(max_length=255)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15)
    company = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, choices=subject_choice)
    budget = models.CharField(max_length=30, choices=budget_choice)
