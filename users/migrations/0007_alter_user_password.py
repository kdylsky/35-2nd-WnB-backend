# Generated by Django 4.0.6 on 2022-11-20 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_kakao_id_remove_user_kakao_profile_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=300),
        ),
    ]
