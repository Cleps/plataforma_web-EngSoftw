# Generated by Django 4.2.3 on 2023-08-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0002_lista_delete_relatorio'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='texto',
            field=models.TextField(default=' '),
        ),
    ]