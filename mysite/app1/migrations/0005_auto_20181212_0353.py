# Generated by Django 2.2.dev20181205203023 on 2018-12-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_articles_agreement_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='agreement_index',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='articlesimilarity',
            name='similarity_percentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='reliability_index',
            field=models.FloatField(),
        ),
    ]