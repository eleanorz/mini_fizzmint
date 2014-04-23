# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name=b'Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'name', models.CharField(max_length=100)),
                (b'title', models.CharField(max_length=100)),
                (b'created_at', models.DateTimeField()),
            ],
            options={
                'db_table': b'managers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'manager', models.ForeignKey(to=b'emp_listing.Manager', to_field='id')),
                (b'name', models.CharField(max_length=100)),
                (b'created_at', models.DateTimeField()),
            ],
            options={
                'db_table': b'employees',
            },
            bases=(models.Model,),
        ),
    ]
