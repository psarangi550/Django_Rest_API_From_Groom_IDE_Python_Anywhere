import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Deploy_WFMT_To_Python_Anywhere.settings')
import django
django.setup()

import random
import faker
import string

from Deploy_WFMT_To_Python_Anywhere_App.models import WFMTTaskModel

# fcp_number_first='CP00'
# fcp_number_middle=str(random.randint(11,99))
# fcp_number_last=''.join([random.choice(string.ascii_uppercase) for _ in range(2)])
# fcp_number=fcp_number_first+fcp_number_middle+fcp_number_last
# fsne_id=random.randint(111111,999999)
# fscheme_number=random.randint(111111,555555)
# ftrs=''.join([random.choice(string.ascii_uppercase) for _ in range(2)])
# festimate_first='WV'
# festimate_middle=str(random.randint(1111,9999))
# festimate_last=''.join([random.choice(string.ascii_uppercase) for _ in range(3)])
# festimate=festimate_first+festimate_middle+fcp_number_last
# print(festimate)

def populate(n):
    for i in range(n):
        fcp_number_first='CP00'
        fcp_number_middle=str(random.randint(11,99))
        fcp_number_last=''.join([random.choice(string.ascii_uppercase) for _ in range(2)])
        fcp_number=fcp_number_first+fcp_number_middle+fcp_number_last
        fsne_id=random.randint(111111,999999)
        fscheme_number=random.randint(200000,400000)
        ftrs=''.join([random.choice(string.ascii_uppercase) for _ in range(2)])
        festimate_first='WV'
        festimate_middle=str(random.randint(1111,9999))
        festimate_last=''.join([random.choice(string.ascii_uppercase) for _ in range(3)])
        festimate=festimate_first+festimate_middle+fcp_number_last
        WFMTTaskModel.objects.get_or_create(cp_number=fcp_number,sne_id=fsne_id,scheme_number=fscheme_number,trs=ftrs,estimate=festimate)

populate(100)

