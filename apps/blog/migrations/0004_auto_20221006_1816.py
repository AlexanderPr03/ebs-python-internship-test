# Generated by Django 3.1.14 on 2022-10-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='blog_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]