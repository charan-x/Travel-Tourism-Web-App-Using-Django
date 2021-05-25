from explore.models import Flight, Pay, Querie
from django.contrib import admin
from explore.models import Flight
from explore.models import Querie
from explore.models import NetPay
from explore.models import Hotel
from explore.models import Train
from explore.models import Bus
# Register your models here.
admin.site.register(Flight)
admin.site.register(Querie)
admin.site.register(Pay)
admin.site.register(NetPay)
admin.site.register(Hotel)
admin.site.register(Train)
admin.site.register(Bus)