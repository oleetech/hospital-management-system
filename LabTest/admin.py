from django.contrib import admin
from .models import Test, Lab, TestSchedule, TestResult

class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')  # Add other fields if needed
    search_fields = ['name']  # Add fields you want to search by

admin.site.register(Test, TestAdmin)

class LabAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Add other fields if needed
    search_fields = ['name']  # Add fields you want to search by

admin.site.register(Lab, LabAdmin)

class TestScheduleAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test', 'lab', 'scheduled_date', 'is_completed')
    search_fields = ['patient__name', 'test__name', 'lab__name']  # Add fields you want to search by
    list_filter = ['lab', 'is_completed', 'scheduled_date']  # Add filters you want to apply

admin.site.register(TestSchedule, TestScheduleAdmin)

class TestResultAdmin(admin.ModelAdmin):
    list_display = ('test_schedule', 'result')
    search_fields = ['test_schedule__patient__name']  # Add fields you want to search by

admin.site.register(TestResult, TestResultAdmin)

