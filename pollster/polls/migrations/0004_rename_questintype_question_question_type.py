# Generated by Django 3.2.4 on 2021-06-28 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_questintype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questintype',
            new_name='question_type',
        ),
    ]