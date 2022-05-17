# Generated by Django 4.0.4 on 2022-05-17 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modulo',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='modulo',
            name='descricao',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modulo',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modulo',
            name='publico',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
