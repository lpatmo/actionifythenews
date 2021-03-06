# Generated by Django 2.1.2 on 2018-10-06 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleTitle', models.CharField(max_length=1000)),
                ('URL', models.CharField(max_length=1000)),
                ('eventID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Event')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Article')),
                ('tagId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Tag')),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='eventID',
        ),
        migrations.RemoveField(
            model_name='newstag',
            name='newsId',
        ),
        migrations.RemoveField(
            model_name='newstag',
            name='tagId',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='NewsTag',
        ),
    ]
