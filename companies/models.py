from django.db import models


class Company(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    address = models.CharField(null=False, blank=False, max_length=250)
    registration_number = models.CharField(null=False, blank=False, max_length=50)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
