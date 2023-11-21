# Generated by Django 4.2.7 on 2023-11-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blinddate', '0004_alter_profile_user_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('non_binary', 'Non-Binary'), ('all', 'All')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='looking_for_gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('non_binary', 'Non-Binary'), ('all', 'All')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_foto',
            field=models.ImageField(blank=True, null=True, upload_to='blinddate/static/media/profileImages/'),
        ),
    ]
