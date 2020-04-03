# Generated by Django 3.0.4 on 2020-04-02 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizApp', '0002_question_image'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attempted',
            options={'verbose_name_plural': 'Attempted Quizzes'},
        ),
        migrations.AlterField(
            model_name='attempted',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.Quiz'),
        ),
        migrations.AlterField(
            model_name='attempted',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]