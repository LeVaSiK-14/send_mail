from django.db import models


class SendMail(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=255)
    is_looked = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} -- {self.date}'
