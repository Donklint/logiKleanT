# Generated by Django 4.2.3 on 2023-08-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerTable',
            fields=[
                ('logi_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('logi_user_firstname', models.CharField(max_length=45)),
                ('logi_user_middlename', models.CharField(max_length=45)),
                ('logi_user_familyname', models.CharField(max_length=45)),
                ('logi_user_email', models.CharField(max_length=45)),
                ('logi_user_mobile', models.CharField(max_length=45)),
            ],
        ),
    ]
