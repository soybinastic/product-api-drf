# Generated by Django 4.1.7 on 2023-06-25 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_table_alter_productcategory_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desciption',
            new_name='description',
        ),
    ]
