# Generated by Django 3.1.6 on 2021-03-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Status', models.CharField(choices=[('pending', 'Pending'), ('Out of delivery', 'Out of delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Price', models.FloatField(null=True)),
                ('Category', models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=100, null=True)),
                ('Description', models.CharField(max_length=200, null=True)),
                ('Date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
