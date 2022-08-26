# Generated by Django 3.0.1 on 2020-01-09 05:19

import StratBook.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StratBook', '0002_auto_20191227_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='team',
            field=models.CharField(choices=[('T', 'Terrorist'), ('CT', 'Counter-Terrorist')], max_length=2),
        ),
        migrations.CreateModel(
            name='Nade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nade_type', models.CharField(choices=[('F', 'Flash'), ('S', 'Smoke'), ('M', 'Molotov'), ('N', 'HE Grenade')], max_length=1)),
                ('img_link', models.URLField(blank=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=StratBook.models.nade_directory_path)),
                ('map_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='StratBook.Map')),
            ],
        ),
    ]