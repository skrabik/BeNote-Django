# Generated by Django 4.2.1 on 2023-05-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_content_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название записки')),
                ('text', models.TextField(blank=True, verbose_name='Текст записки')),
                ('user_id', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('last_time_update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('date_delete', models.DateTimeField(auto_now_add=True, verbose_name='Дата удаления')),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='last_time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='content',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст записки'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название записки'),
        ),
    ]