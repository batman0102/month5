# Generated by Django 5.0.6 on 2024-05-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=3),
        ),
    ]