from django.contrib import admin

from .models import Hospital, Department, Room, Bed,Ward

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    pass

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    pass