# Generated by Django 2.2.2 on 2019-07-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20190703_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user_created',
            field=models.CharField(default='emmabean', max_length=40),
            preserve_default=False,
        ),
    ]
