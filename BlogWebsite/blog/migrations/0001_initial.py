# Generated by Django 4.2.8 on 2023-12-08 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('ID', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('ID', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Date_Published', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('ID', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Date_Posted', models.DateTimeField()),
                ('Post_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', unique=True)),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.user', unique=True)),
            ],
        ),
    ]