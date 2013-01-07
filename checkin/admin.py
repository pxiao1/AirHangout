from checkin.models import singleFlightRecord
from checkin.models import currentData
from checkin.models import client
from django.contrib import admin
    
admin.site.register(singleFlightRecord)
admin.site.register(currentData)
admin.site.register(client)
#admin.site.register(Choice)
