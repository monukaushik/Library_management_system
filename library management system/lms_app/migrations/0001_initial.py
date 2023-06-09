# Generated by Django 3.2.12 on 2023-01-31 07:26

from django.db import migrations, models
import lms_app.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookdetail',
            fields=[
                ('bookid', models.AutoField(primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=200)),
                ('stuname', models.CharField(max_length=200, null=True)),
                ('sturollno', models.IntegerField(null=True)),
                ('bookimage', models.ImageField(upload_to='images/')),
                ('bookauthor', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('Qty', models.IntegerField()),
                ('requiredqty', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=100)),
                ('issuedate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('studentimg', models.ImageField(upload_to='images/')),
                ('studentbranch', models.CharField(max_length=100)),
                ('studentrollno', models.IntegerField(blank=True, null=True)),
                ('studentadd1', models.CharField(max_length=200)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', lms_app.manager.CustomuserdetailManager()),
            ],
        ),
    ]
