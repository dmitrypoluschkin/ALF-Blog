# Generated by Django 5.1 on 2024-08-13 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='emai',
            new_name='email',
        ),
    ]
