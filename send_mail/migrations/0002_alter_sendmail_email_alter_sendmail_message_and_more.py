# Generated by Django 4.0.1 on 2022-01-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmail',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sendmail',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sendmail',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sendmail',
            name='position',
            field=models.CharField(max_length=255),
        ),
    ]
