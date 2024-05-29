from django.db import models
from django.contrib.auth.models import User

class ActivationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
