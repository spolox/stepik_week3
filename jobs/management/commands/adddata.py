import os

from django.core.management.base import BaseCommand

from jobs.models import Specialty, Company, Vacancy
from stepik_hh.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR


class Command(BaseCommand):
    help = 'Write new data to database from <filename>.\n' \
           'Filename should contain lists of jobs, companies, specialties'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filename', help="File with new data for database")

    def handle(self, *args, **options):
        filename = os.path.splitext(options['filename'])
        if filename[1] == '.py':
            module = __import__(filename[0])
        else:
            raise Exception('This is not python file. Use python file with data')
        if 'specialties' in dir(module):
            for specialty in module.specialties:
                if Specialty.objects.filter(code=specialty['code']).first() is None:
                    Specialty.objects.create(
                        code=specialty['code'],
                        title=specialty['title'],
                        picture=os.path.join(MEDIA_SPECIALITY_IMAGE_DIR, 'specty_' + specialty['code'] + '.png'),
                    )
        if 'companies' in dir(module):
            for company in module.companies:
                Company.objects.create(
                    name=company['title'],
                    location=company['location'],
                    description=company['description'],
                    employee_count=company['employee_count'],
                    logo=os.path.join(MEDIA_COMPANY_IMAGE_DIR, company['logo']),
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
