# Generated by Django 3.2.7 on 2021-09-06 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_contato_fotos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='fotos',
            new_name='foto',
        ),
    ]
