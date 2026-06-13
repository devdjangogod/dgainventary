from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_patrimonial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bieninventario',
            name='dni',
            field=models.CharField(default='00000000', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bieninventario',
            name='sede_filial',
            field=models.CharField(default='SIN SEDE', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bieninventario',
            name='usuario_responsable',
            field=models.CharField(default='PRINCIPAL', max_length=150),
            preserve_default=False,
        ),
    ]