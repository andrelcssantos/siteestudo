# Generated by Django 2.1 on 2018-09-03 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180903_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movmensalista',
            old_name='veiculo',
            new_name='mensalista',
        ),
    ]