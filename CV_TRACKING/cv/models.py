from django.db import models

from django.contrib.auth.models import User

# Create your models here.

APPLICATION_ANSWER = (
    (1, 'Rejected'),
    (2, 'Accepted'),
    (3, 'Next Stage '),
)


class Company(models.Model):
    name = models.CharField(max_length=164, blank=False)
    work_position = models.CharField(blank=False, default='python developer')


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(on_delete=models.CASCADE)
    post_date = models.DateField(blank=False)
    position = models.ForeignKey(on_delete=models.CASCADE, blank=False)
    salary = models.SmallIntegerField(blank=False, default=3000)
    reply = models.CharField(choices=APPLICATION_ANSWER, default='Rejected', blank=False)
    reply_date = models.DateField()
    other = models.TextField(max_length=256)


