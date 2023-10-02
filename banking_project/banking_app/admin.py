from django.contrib import admin
from .models import Details,Material,District,Branch
# Register your models here.
admin.site.register(Details)
admin.site.register(Material)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(District)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name','slug','district']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','stock','available']

admin.site.register(Branch)

