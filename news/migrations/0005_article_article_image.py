# Generated by Django 4.0.3 on 2022-03-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='timezone.now', upload_to='articles/'),
        ),
    ]