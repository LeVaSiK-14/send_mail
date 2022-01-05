from send_mail.views import SendMailModelViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('mails', SendMailModelViewSet)

urlpatterns = []

urlpatterns += router.urls