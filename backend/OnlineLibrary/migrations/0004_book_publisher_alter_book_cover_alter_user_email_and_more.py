# Generated by Django 5.0.4 on 2024-05-20 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineLibrary', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='OnlineLibrary.user'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='covers/cover_default.png', null=True, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='isAdmin',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='photos\\photo_default.png"', null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='borrowtransaction',
            unique_together={('user', 'book')},
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'book')},
        ),
    ]
