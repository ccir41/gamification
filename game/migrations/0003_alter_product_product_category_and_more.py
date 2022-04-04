# Generated by Django 4.0.3 on 2022-04-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('ELECTRONICS', 'Electronics'), ('FURNITURE', 'Furniture')], default='ELECTRONICS', max_length=64),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]
