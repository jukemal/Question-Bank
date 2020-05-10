# Generated by Django 3.0.6 on 2020-05-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='%Y/%m/%d/')),
                ('answer_1', models.CharField(max_length=500)),
                ('answer_2', models.CharField(max_length=500)),
                ('answer_3', models.CharField(max_length=500)),
                ('answer_4', models.CharField(max_length=500)),
                ('correct_answer', models.IntegerField(choices=[(1, 'Answer 1'), (2, 'Answer 2'), (3, 'Answer 3'), (4, 'Answer 4')])),
            ],
        ),
    ]