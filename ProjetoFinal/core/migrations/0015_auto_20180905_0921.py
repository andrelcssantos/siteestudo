# Generated by Django 2.1 on 2018-09-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180905_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalista',
            name='veiculo',
            field=models.ForeignKey(on_delete=False, to='core.Veiculo'),
        ),
        migrations.AlterField(
            model_name='movmensalista',
            name='mensalista',
            field=models.ForeignKey(on_delete=False, to='core.Mensalista'),
        ),
        migrations.AlterField(
            model_name='movrotativo',
            name='veiculo',
            field=models.ForeignKey(on_delete=False, to='core.Veiculo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(on_delete=False, to='core.Marca'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='proprietario',
            field=models.ForeignKey(on_delete=False, to='core.Pessoa'),
        ),
    ]