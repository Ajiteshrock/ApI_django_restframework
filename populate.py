import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','intern.settings')

import django
# Import settings
django.setup()

import random
from api.models import user
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_user_name = fakegen.name()
        fake_user_id = fakegen.random_int()
        user_start = fakegen.date()
        user_end = fakegen.date_this_year()
        tz = fakegen.address()
        # Create new User Entry
        user1 = user.objects.get_or_create(user_name=fake_user_name,
                                          user_id = fake_user_id,
                                          user_end_date = user_end,
                                          user_tz = tz,
                                          user_startdate=user_start)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(30)
    print('Populating Complete')
