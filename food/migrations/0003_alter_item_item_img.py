# Generated by Django 4.0.4 on 2023-02-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_img',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.everestkitchenpa.com%2Fassets%2Fpages%2FcoldBeverages.html&psig=AOvVaw0EOhjaJvqv0I6_sRj0h9Sf&ust=1676898737183000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCPiK9NbWof0CFQAAAAAdAAAAABAJ', max_length=500),
        ),
    ]
