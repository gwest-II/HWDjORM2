# Generated by Django 4.0.6 on 2022-07-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_articlescope_is_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]