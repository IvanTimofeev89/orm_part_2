# Generated by Django 5.0 on 2023-12-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_options_scope_tag_scope_id_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AddField(
            model_name='article',
            name='posts',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag'),
        ),
    ]
