# Generated by Django 4.2.9 on 2024-01-31 14:41

from django.db import migrations
from phonenumber_field.phonenumber import PhoneNumber


def migrate_phone_numbers(apps, schema_editor):
    CustomUser = apps.get_model('customuser', 'CustomUser')
    default_phone_number = PhoneNumber.from_string('+46708511669')  # Set your desired default phone number here
    for customuser in CustomUser.objects.all():
        if customuser.phone_number is None:  # Check if phone_number is None
            customuser.phone_number = default_phone_number
            customuser.save()

class Migration(migrations.Migration):
    dependencies = [
        ('customuser', '0004_auto_20240131_1418'),
    ]

    operations = [
        migrations.RunPython(migrate_phone_numbers),
    ]