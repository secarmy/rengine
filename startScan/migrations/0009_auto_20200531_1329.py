# Generated by Django 3.0.6 on 2020-05-31 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0008_scannedsubdomainwithprotocols_http_header_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scannedhost',
            name='takeover_possible',
        ),
        migrations.AddField(
            model_name='scannedhost',
            name='content_length',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scannedhost',
            name='http_status',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scannedhost',
            name='page_title',
            field=models.CharField(default='Hello Hello', max_length=1000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ScannedSubdomainWithProtocols',
        ),
    ]
