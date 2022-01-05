from django.contrib import admin
from send_mail.models import SendMail

class SendMailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'is_looked', 'position')

admin.site.register(SendMail, SendMailAdmin)
