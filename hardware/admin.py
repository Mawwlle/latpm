from django.contrib import admin

from hardware.models import Computer, CPUInfo, GPUInfo

# Register your models here.
admin.site.register(Computer)
admin.site.register(CPUInfo)
admin.site.register(GPUInfo)
