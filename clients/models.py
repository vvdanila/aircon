from django.db import models


class Client(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    address = models.CharField(null=False, blank=False, max_length=250)
    client_id = models.CharField(null=False, blank=False, max_length=50)

    class Meta:
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name
