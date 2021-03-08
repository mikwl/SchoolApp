# Generated by Django 3.1.7 on 2021-03-08 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=250, verbose_name='Название / номер группы')),
                ('group_facultet', models.CharField(max_length=250, verbose_name='Факультет')),
            ],
        ),
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predmet_name', models.CharField(max_length=250, verbose_name='Название предмета')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=250, verbose_name='Название школы')),
                ('school_location', models.CharField(max_length=250, verbose_name='Адрес школы')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_first_name', models.CharField(max_length=250, verbose_name='Имя учащегося')),
                ('student_last_name', models.CharField(max_length=250, verbose_name='Фамилия учащегося')),
                ('student_age', models.IntegerField(verbose_name='Возраст учащегося')),
                ('student_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.group', verbose_name='Группа')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school', verbose_name='Школа'),
        ),
    ]