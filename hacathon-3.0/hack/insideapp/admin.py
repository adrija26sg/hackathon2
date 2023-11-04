from django.contrib import admin
from insideapp import models
from .models import useraccountregister
from .models import workeraccountregister,loginpage,center1,center2,center3,center4,center5,center6,order   
 
admin.site.register(useraccountregister)
admin.site.register(workeraccountregister)
admin.site.register(loginpage)
admin.site.register(center1)
admin.site.register(center2)
admin.site.register(center3)
admin.site.register(center4)
admin.site.register(center5)
admin.site.register(center6)
admin.site.register(order)

# Register your models here.
