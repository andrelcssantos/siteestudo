# Generated by Django 2.1 on 2018-09-05 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180905_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalista',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo'),
        ),
    ]