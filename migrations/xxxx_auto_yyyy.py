from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('pise', 'previous_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='establecimiento',
            name='nombramiento_encargado_convivencia',
            field=models.FileField(blank=True, null=True, upload_to='nombramiento_encargado_convivencia/'),
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='plan_gestion_convivencia',
            field=models.FileField(blank=True, null=True, upload_to='plan_gestion_convivencia/'),
        ),
    ] 