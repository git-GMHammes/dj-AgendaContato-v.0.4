# Generated by Django 4.0 on 2021-12-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appContatos', '0003_rename_varnome_dbtabcategoria_strnome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbtabcontatos',
            name='strTelefone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]