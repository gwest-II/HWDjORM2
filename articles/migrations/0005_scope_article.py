# Generated by Django 4.0.6 on 2022-07-28 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_options_alter_articlescope_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='article',
            field=models.ManyToManyField(through='articles.ArticleScope', to='articles.article'),
        ),
    ]
