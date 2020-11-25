import os
import sys

from django.core.files import File
from django.core.management.base import BaseCommand

from jobs.models import Specialty, Company, Vacancy


class Command(BaseCommand):
    directory = ''

    BaseCommand.help = 'Write new data to database from <filename>.\n' \
                       'Filename should contain lists of jobs, companies, specialties'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filename', help="File with new data for database")

    def add_specialities(self, specialties):
        for specialty in specialties:
            if Specialty.objects.filter(code=specialty['code']).first() is None:
                specialty_img_filename = 'specty_' + specialty['code'] + '.png'
                with open(os.path.join(self.directory, specialty_img_filename), 'rb') as specialty_img_file:
                    Specialty.objects.create(
                        code=specialty['code'],
                        title=specialty['title'],
                        picture=File(specialty_img_file, specialty_img_filename),
                    )

    def add_companies(self, companies):
        for company in companies:
            with open(os.path.join(self.directory, company['logo']), 'rb') as logo_img_file:
                Company.objects.create(
                    name=company['title'],
                    location=company['location'],
                    description=company['description'],
                    employee_count=company['employee_count'],
                    logo=File(logo_img_file, company['logo']),
                )

    def add_jobs(self, jobs):
        for job in jobs:
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

    def handle(self, *args, **options):
        file_full_path = options['filename']
        self.directory = os.path.dirname(file_full_path)
        if self.directory:
            sys.path.append(self.directory)
        (filename, ext) = os.path.splitext(os.path.basename(file_full_path))
        module_data = __import__(filename)
        if 'specialties' in dir(module_data):
            self.add_speciality(module_data.specialties)
        if 'companies' in dir(module_data):
            self.add_companies(module_data.companies)
        if 'jobs' in dir(module_data):
            self.add_jobs(module_data.jobs)
