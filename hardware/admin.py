from django.contrib import admin

from hardware.models import ComputerModel, CPUInfoModel, GPUInfoModel

# Register your models here.
admin.site.register(ComputerModel)
admin.site.register(CPUInfoModel)
admin.site.register(GPUInfoModel)
