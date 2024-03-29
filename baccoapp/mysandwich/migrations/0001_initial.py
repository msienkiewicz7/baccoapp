# Generated by Django 2.2 on 2019-06-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('BREAD', 'Bread'), ('BASE', 'Base'), ('CHEESE', 'Cheese'), ('VEGETABLE', 'Vegetable'), ('CONDIMENT', 'Contiment'), ('EXTRAS', 'Extras')], max_length=50)),
                ('calories', models.IntegerField(default=0)),
                ('is_vegetarian', models.BooleanField()),
                ('is_vegan', models.BooleanField()),
                ('img', models.FileField(upload_to='ingredients')),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='date created')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ingredients', models.ManyToManyField(to='mysandwich.Ingredient')),
            ],
        ),
    ]
