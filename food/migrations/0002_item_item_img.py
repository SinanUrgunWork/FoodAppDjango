# Generated by Django 4.0.4 on 2023-02-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_img',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Ftoppng.com%2Ffree-image%2Fclipart-free-seaweed-clipart-draw-food-placeholder-PNG-free-PNG-Images_183132&psig=AOvVaw0EOhjaJvqv0I6_sRj0h9Sf&ust=1676898737183000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCODX197Uof0CFQAAAAAdAAAAABAE', max_length=500),
        ),
    ]
