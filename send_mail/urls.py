from send_mail.views import index, send
# from rest_framework.routers import SimpleRouter
from django.urls import path

# router = SimpleRouter()

# router.register('mails', SendMailModelViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('form/', send, name='form')
]

# urlpatterns += router.urls