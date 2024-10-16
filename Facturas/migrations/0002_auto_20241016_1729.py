# Generated by Django 3.2.6 on 2024-10-16 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Colegios', '0001_initial'),
        ('Facturas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CronogramaDePago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Colegios.colegio')),
                ('cursos', models.ManyToManyField(to='Colegios.Curso')),
            ],
        ),
        migrations.AlterField(
            model_name='factura',
            name='fechaIni',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fechaVen',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='DetalleCronograma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.IntegerField()),
                ('fechaCausacion', models.DateField()),
                ('fechaLimite', models.DateField()),
                ('cronograma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Facturas.cronogramadepago')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='cronograma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Facturas.cronogramadepago'),
        ),
    ]
