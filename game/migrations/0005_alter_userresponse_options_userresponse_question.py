# Generated by Django 4.0.3 on 2022-04-05 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_product_max_price_alter_product_min_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userresponse',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='userresponse',
            name='question',
            field=models.ManyToManyField(blank=True, to='game.product'),
        ),
    ]
