import os
import sys

from PIL import Image
from django.core.management.base import BaseCommand
from django.core.files import File

from jobs.models import Specialty, Company, Vacancy
from stepik_hh.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR


class Command(BaseCommand):
    help = 'Write new data to database from <filename>.\n' \
           'Filename should contain lists of jobs, companies, specialties'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filename', help="File with new data for database")

    def handle(self, *args, **options):
        full_path_file = options['filename']
        directory = os.path.dirname(full_path_file)
        if directory:
            sys.path.append(directory)
        (filename, ext) = os.path.splitext(os.path.basename(full_path_file))
        if ext == '.py':
            module = __import__(filename)
        else:
            raise Exception('This is not python file. Use python file with data')
        if 'specialties' in dir(module):
            for specialty in module.specialties:
                if Specialty.objects.filter(code=specialty['code']).first() is None:
                    specialty_img_filename = 'specty_' + specialty['code'] + '.png'
                    with open(os.path.join(directory,specialty_img_filename), 'rb') as specialty_img_file:
                        Specialty.objects.create(
                            code=specialty['code'],
                            title=specialty['title'],
                            picture=File(specialty_img_file, specialty_img_filename),
                        )
        if 'companies' in dir(module):
            for company in module.companies:
                with open(os.path.join(directory, company['logo']), 'rb') as company_img_file:
                    Company.objects.create(
                        name=company['title'],
                        location=company['location'],
                        description=company['description'],
                        employee_count=company['employee_count'],
                        logo=File(company_img_file, company['logo']),
                    )
        if 'jobs' in dir(module):
            for job in module.jobs:
                Vacancy.objects.create(
                    title=job['title'],
                    specialty=Specialty.objects.get(code=job['specialty']),
                    company=Company.objects.get(pk=job['company']),
                    skills=job['skills'],
                    description=job['description'],
                    salary_min=job['salary_from'],
                    salary_max=job['salary_to'],
                    published_at=job['posted'],
                )
        print('New data are added')
