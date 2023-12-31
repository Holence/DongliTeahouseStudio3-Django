# Generated by Django 4.2 on 2023-06-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('texts', '0001_initial'),
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('attachments', models.ManyToManyField(blank=True, related_name='concepts', to='attachments.attachment')),
                ('childs', models.ManyToManyField(blank=True, related_name='parents', to='concepts.concept')),
                ('relatives', models.ManyToManyField(blank=True, to='concepts.concept')),
                ('texts', models.ManyToManyField(blank=True, related_name='concepts', to='texts.text')),
            ],
        ),
    ]
