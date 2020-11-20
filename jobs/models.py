from django.db import models

from stepik_hh.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR


class Specialty(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=20)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR, height_field='height_field',
                                width_field='width_field')
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, height_field='height_field', width_field='width_field')
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    description = models.TextField()
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=255)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
