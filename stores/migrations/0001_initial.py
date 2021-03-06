# Generated by Django 2.0.2 on 2018-02-05 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_name', models.CharField(max_length=100)),
                ('products_detail', models.CharField(max_length=200)),
                ('products_price', models.IntegerField(default=0)),
                ('products_stars', models.IntegerField(default=0)),
                ('products_pub_date', models.DateTimeField(verbose_name='date published')),
                ('viewers', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Review_pub_date', models.DateTimeField(verbose_name='date published')),
                ('Review_text', models.CharField(max_length=200)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stores_name', models.CharField(max_length=20)),
                ('stores_stars', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Stores'),
        ),
    ]
