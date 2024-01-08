from django import forms

from django_recaptcha.fields import ReCaptchaField

class FormWithCaptcha(forms.Form):
    name = forms.EmailField()
    captcha = ReCaptchaField()