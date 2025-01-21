# Generated by Django 5.1.4 on 2025-01-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOK_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=122)),
                ('Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Person', models.IntegerField()),
                ('Date', models.DateField()),
            ],
        ),
    ]
