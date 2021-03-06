# Generated by Django 3.0.4 on 2020-04-12 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('issue', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(default='unresolved', max_length=20)),
                ('description', models.CharField(default='No issue reported', max_length=200)),
                ('time', models.IntegerField(default=1)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change', models.CharField(max_length=100)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Issue')),
            ],
        ),
    ]
