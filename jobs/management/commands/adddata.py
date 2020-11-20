import os

from django.core.management.base import BaseCommand

from jobs.models import Specialty, Company, Vacancy
from stepik_hh.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR


class Command(BaseCommand):
    help = 'Write new data to database from <filename>.\n' \
           'Filename must contain lists of jobs, companies, specialties'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filename', help="File with new data for database")

    def handle(self, *args, **options):
        filename = os.path.splitext(options['filename'])
        if filename[1] == '.py':
            module = __import__(filename[0])
        else:
            raise Exception('This is not python file. Use python file with data')
        if 'companies' not in dir(module):
            raise Exception('Not found companies in module')
        if 'jobs' not in dir(module):
            raise Exception('Not found jobs in module')
        if 'specialties' not in dir(module):
            raise Exception('Not found specialties in module')
        for specialty in module.specialties:
            if Specialty.objects.filter(code=specialty['code']).first() is None:
                Specialty.objects.create(
                    code=specialty['code'],
                    title=specialty['title'],
                    picture=os.path.join(MEDIA_SPECIALITY_IMAGE_DIR, 'specty_' + specialty['code'] + '.png'),
                )
        for company in module.companies:
            if Company.objects.filter(id=company['id']).first() is None:
                Company.objects.create(
                    pk=company['id'],
                    name=company['title'],
                    location=company['location'],
                    description=company['description'],
                    employee_count=company['employee_count'],
                    logo=os.path.join(MEDIA_COMPANY_IMAGE_DIR, company['logo']),
                )
        for job in module.jobs:
            if Vacancy.objects.filter(id=job['id']).first() is None:
                Vacancy.objects.create(
                    pk=job['id'],
                    title=job['title'],
                    specialty=Specialty.objects.get(code=job['specialty']),
                    company=Company.objects.get(pk=job['company']),
                    skills=job['skills'],
                    description=job['description'],
                    salary_min=job['salary_from'],
                    salary_max=job['salary_to'],
                    published_at=job['posted'],
                )
        print('Create database is finished')
