# Generated by Django 3.1.8 on 2022-01-23 21:36

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("djangocms_frontend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Accordion",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="AccordionItem",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
    ]
