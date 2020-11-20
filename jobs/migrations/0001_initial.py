from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('logo', models.ImageField(height_field='height_field',
                                           upload_to='company_images', width_field='width_field')),
                ('height_field', models.PositiveIntegerField(default=0)),
                ('width_field', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
                ('employee_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('picture', models.ImageField(height_field='height_field', upload_to='speciality_images',
                                              width_field='width_field')),
                ('height_field', models.PositiveIntegerField(default=0)),
                ('width_field', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('salary_min', models.IntegerField()),
                ('salary_max', models.IntegerField()),
                ('published_at', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies',
                                              to='jobs.company')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies',
                                                to='jobs.specialty')),
            ],
        ),
    ]
