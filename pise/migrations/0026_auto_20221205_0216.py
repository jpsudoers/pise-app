# Generated by Django 3.2.9 on 2022-12-05 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pise', '0025_auto_20221012_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='connotacionsexual',
            name='archivo_declaracion_individual',
            field=models.FileField(blank=True, null=True, upload_to='declaracion_individual/ConnotacionSexual'),
        ),
        migrations.AddField(
            model_name='connotacionsexual',
            name='denunciante',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maltrato',
            name='archivo_declaracion_individual',
            field=models.FileField(blank=True, null=True, upload_to='declaracion_individual/maltrato'),
        ),
        migrations.AddField(
            model_name='maltrato',
            name='denunciante',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vulneracionderechosfuncionarios',
            name='archivo_declaracion_individual',
            field=models.FileField(blank=True, null=True, upload_to='declaracion_individual/vulneracion'),
        ),
        migrations.AddField(
            model_name='vulneracionderechosfuncionarios',
            name='denunciante',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='maltrato',
            name='tipo_maltrato',
            field=models.CharField(choices=[('Hacia Menor', (('adulto', 'Adulto a Menor'), ('menor', 'Menor a Menor'))), ('Hacia Adulto', (('alumno_docente', 'Alumno a Docente o Funcionarios'), ('apoderado', 'Apoderado a Docente o Funcionarios')))], default='estudiante', max_length=255, null=True),
        ),
    ]
