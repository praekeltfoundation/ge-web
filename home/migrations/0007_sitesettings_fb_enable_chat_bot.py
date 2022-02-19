# Generated by Django 4.0.2 on 2022-02-18 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_social_media_site_structblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='fb_enable_chat_bot',
            field=models.BooleanField(default=False, help_text='Activate chat-bot for facebook messenger.'),
        ),
    ]
