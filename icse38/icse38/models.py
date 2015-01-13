from django.db import models


class Submission(models.Model):
    sub_name = models.CharField(max_length=200)
	sub_affiliation = models.CharField(max_length=200)
	sub_video = models.CharField(max_length=200)
    sub_acceptance = models.IntegerField(default=0)