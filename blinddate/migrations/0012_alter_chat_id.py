# Generated by Django 4.2.7 on 2023-11-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blinddate', '0011_chat_receiver_chat_sender_chat_text_alter_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]