from rest_framework import serializers
from send_mail.models import SendMail
from send_mail.tasks import send_mail_to_email


class SendMailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SendMail
        fields = ['name', 'email', 'position', 'message']

    def create(self, validated_data):
        send_mail_to_email.delay(
            validated_data['name'],
            validated_data['email'],
            validated_data['message'],
            validated_data['position'])
        mail = SendMail.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            message=validated_data['message'],
            position=validated_data['position'])
        return mail
