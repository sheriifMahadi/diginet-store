# Generated by Django 4.2.7 on 2023-11-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_alter_product_options_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('waitingapproval', 'Waiting approval'), ('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=50),
        ),
    ]
