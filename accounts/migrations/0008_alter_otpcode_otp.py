# Generated by Django 5.0.2 on 2024-03-03 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_otpcode_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='otp',
            field=models.CharField(default='83c6e', max_length=6),
        ),
    ]