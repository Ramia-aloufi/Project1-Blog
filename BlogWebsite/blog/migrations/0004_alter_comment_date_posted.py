# Generated by Django 4.2.8 on 2023-12-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_user_id_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Date_Posted',
            field=models.DateField(auto_now_add=True),
        ),
    ]
