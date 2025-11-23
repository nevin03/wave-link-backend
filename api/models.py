from django.db import models

class TermsAndConditions(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.__class__.objects.all().delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Terms & Conditions"

class PrivacyPolicy(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.__class__.objects.all().delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Privacy Policy"
