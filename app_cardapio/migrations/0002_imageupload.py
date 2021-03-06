# Generated by Django 2.2 on 2020-08-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cardapio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('arquivo', models.ImageField(upload_to='images/%d-%m-%Y/')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Data de Publicação')),
            ],
            options={
                'verbose_name_plural': 'Lista',
            },
        ),
    ]
