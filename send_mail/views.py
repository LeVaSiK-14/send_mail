from send_mail.serializers import SendMailSerializer
from send_mail.models import SendMail
from rest_framework.viewsets import ModelViewSet


class SendMailModelViewSet(ModelViewSet):
    queryset = SendMail.objects.all()
    serializer_class = SendMailSerializer


