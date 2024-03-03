# Generated by Django 5.0.2 on 2024-03-03 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_otpcode_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='accounts/images/carton.png', null=True, upload_to='accounts/images/%Y/%m/%d/%H/%M/%S/'),
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='otp',
            field=models.CharField(default='47264', max_length=6),
        ),
    ]