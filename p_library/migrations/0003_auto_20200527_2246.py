# Generated by Django 2.2.6 on 2020-05-27 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_book_bookcover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='p_library.Friend'),
        ),
    ]
