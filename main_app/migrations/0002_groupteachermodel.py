# Generated by Django 4.2.6 on 2023-11-13 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTeacherModel',
            fields=[
                ('id', models.BigIntegerField(db_column='id', primary_key=True, serialize=False)),
                ('group_name', models.TextField(db_column='group_name', max_length=100)),
                ('description', models.TextField(db_column='description', max_length=500)),
                ('leader_id', models.BigIntegerField(db_column='leader_id')),
                ('created_at', models.DateTimeField(db_column='created_at')),
                ('updated_at', models.DateTimeField(db_column='updated_at')),
            ],
            options={
                'db_table': 'group_teacher',
            },
        ),
    ]
