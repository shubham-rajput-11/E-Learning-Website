# Generated by Django 4.2.4 on 2023-09-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='files/thumbnail')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('resource', models.FileField(upload_to='files/resource')),
                ('length', models.IntegerField()),
            ],
        ),
    ]