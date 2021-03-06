# Generated by Django 2.2.3 on 2020-11-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.CharField(max_length=120)),
                ('image_url', models.URLField()),
                ('detail_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Kitablar',
                'verbose_name_plural': 'Kitablar',
                'ordering': ['-id'],
            },
        ),
    ]
