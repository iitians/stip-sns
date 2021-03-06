# Generated by Django 1.10.4 on 2018-01-17 01:28


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0012_profile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(default=None, max_length=128, null=True, unique=True)),
                ('local_name', models.CharField(default=None, max_length=128, null=True, unique=True)),
                ('locale', models.CharField(choices=[(b'en', 'English'), (b'pt-br', 'Portuguese'), (b'es', 'Spanish'), (b'ja', 'Japanese'), (b'fr', 'French'), (b'zh-cn', 'Chinese')], default='en', max_length=4)),
                ('description', models.TextField(default=None, max_length=1024, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Profile')),
                ('members', models.ManyToManyField(related_name='Members', to='authentication.Profile')),
            ],
        ),
    ]
