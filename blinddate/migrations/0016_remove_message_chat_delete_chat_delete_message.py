# Generated by Django 4.2.7 on 2023-11-28 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blinddate', '0015_remove_chat_text_remove_chat_timestamp_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
