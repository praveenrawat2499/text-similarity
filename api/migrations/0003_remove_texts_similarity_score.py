# Generated by Django 4.1.6 on 2024-04-02 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_texts_similarity_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='texts',
            name='similarity_score',
        ),
    ]