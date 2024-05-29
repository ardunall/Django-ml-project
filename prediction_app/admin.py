from django.contrib import admin
from .models import DiabetesPrediction

class DiabetesPredictionAdmin(admin.ModelAdmin):
    list_display = ("user",'age', 'sex', 'bmi', 'bp', 'tc', 'ldl', 'hdl', 'tch', 'ltg', 'glucose', 'result')


admin.site.register(DiabetesPrediction, DiabetesPredictionAdmin)
