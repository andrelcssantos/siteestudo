# Generated by Django 2.1 on 2018-09-03 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_movmensalista'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movmensalista',
            old_name='mensalista',
            new_name='veiculo',
        ),
    ]