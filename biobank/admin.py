from django.contrib import admin

from .models import *
# Register your models here.




class heloo(admin.ModelAdmin):
    pass


admin.site.register(Cube,heloo)
admin.site.register(Box,heloo)
admin.site.register(Rack,heloo)
admin.site.register(Freezer,heloo)
admin.site.register(Study,heloo)
admin.site.register(Patient,heloo)
admin.site.register(Sample,heloo)

admin.site.register(Shelf,heloo)
