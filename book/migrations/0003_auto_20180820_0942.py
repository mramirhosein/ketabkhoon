# Generated by Django 2.1 on 2018-08-20 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_read_private_section', 'VIP User'), ('user_watcher', 'User Watcher'))},
        ),
    ]