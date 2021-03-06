# Generated by Django 4.0.5 on 2022-06-27 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_remove_emergencycontact_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='HONOURS_DEGREE_FAZIL',
        ),
        migrations.RemoveField(
            model_name='student',
            name='HSC_ALIM_DIPLOMA',
        ),
        migrations.RemoveField(
            model_name='student',
            name='MASTERS_KAMIL',
        ),
        migrations.RemoveField(
            model_name='student',
            name='SSC_DAKHIL',
        ),
        migrations.RemoveField(
            model_name='student',
            name='passing_year',
        ),
        migrations.CreateModel(
            name='EducationalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSC_DAKHIL', models.CharField(blank=True, max_length=30, null=True)),
                ('HSC_ALIM_DIPLOMA', models.CharField(blank=True, max_length=30, null=True)),
                ('HONOURS_DEGREE_FAZIL', models.CharField(blank=True, max_length=30, null=True)),
                ('MASTERS_KAMIL', models.CharField(blank=True, max_length=30, null=True)),
                ('cgpa_or_gpa', models.FloatField(blank=True, null=True)),
                ('passing_year', models.DateField(blank=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_educational_record', to='student.student')),
            ],
        ),
    ]
