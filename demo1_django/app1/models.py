from django import forms
from django.db import models


# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox


class User1(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=False, blank=False)
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default='', blank=True)

