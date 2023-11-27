# Generated by Django 4.2.7 on 2023-11-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blinddate', '0007_match_match_list_owner_match_matches'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='not_match_but_seen',
            field=models.ManyToManyField(related_name='not_match_but_seen', to='blinddate.profile'),
        ),
        migrations.AlterField(
            model_name='match',
            name='matches',
            field=models.ManyToManyField(related_name='matchlist', to='blinddate.profile'),
        ),
    ]