# Generated by Django 2.1 on 2018-09-03 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180903_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo')),
            ],
        ),
    ]
