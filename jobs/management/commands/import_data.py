import os
import sys

from django.core.files import File
from django.core.management.base import BaseCommand

from jobs.models import Specialty, Company, Vacancy


class Command(BaseCommand):
    BaseCommand.help = 'Write new data to database from <filename>.\n' \
           'Filename should contain lists of jobs, companies, specialties'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filename', help="File with new data for database")

    def handle(self, *args, **options):
        file_full_path = options['filename']
        directory = os.path.dirname(file_full_path)
        if directory:
            sys.path.append(directory)
        (filename, ext) = os.path.splitext(os.path.basename(file_full_path))
        if ext == '.py':
            module_data = __import__(filename)
        else:
            raise Exception('This is not python file. Use python file with data')
        if 'specialties' in dir(module_data):
            for specialty in module_data.specialties:
                if Specialty.objects.filter(code=specialty['code']).first() is None:
                    specialty_img_filename = 'specty_' + specialty['code'] + '.png'
                    with open(os.path.join(directory, specialty_img_filename), 'rb') as specialty_img_file:
                        Specialty.objects.create(
                            code=specialty['code'],
                            title=specialty['title'],
                            picture=File(specialty_img_file, specialty_img_filename),
                        )
        if 'companies' in dir(module_data):
            for company in module_data.companies:
                with open(os.path.join(directory, company['logo']), 'rb') as logo_img_file:
                    Company.objects.create(
                        name=company['title'],
                        location=company['location'],
                        description=company['description'],
                        employee_count=company['employee_count'],
                        logo=File(logo_img_file, company['logo']),
                    )
        if 'jobs' in dir(module_data):
            for job in module_data.jobs:
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
