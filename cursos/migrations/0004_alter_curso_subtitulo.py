# Generated by Django 3.2.11 on 2022-01-25 22:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_auto_20220125_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='subtitulo',
            field=tinymce.models.HTMLField(max_length=200, verbose_name='Subtítulo'),
        ),
    ]
