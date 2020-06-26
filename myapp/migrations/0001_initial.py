# Generated by Django 3.0.7 on 2020-06-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.IntegerField(choices=[(1, 'Category 1'), (2, 'Category 2'), (3, 'Category 3')], default=1)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=300)),
                ('launching_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('is_active', models.IntegerField(blank=True, choices=[(1, 'Active'), (0, 'Inactive')], default=1, help_text='1->Active, 0->Inactive', null=True)),
            ],
            options={
                'ordering': ['-launching_date'],
            },
        ),
    ]