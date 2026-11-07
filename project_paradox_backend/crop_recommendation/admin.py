from django.contrib import admin
from .models import CropRecommendation

@admin.register(CropRecommendation)
class CropRecommendationAdmin(admin.ModelAdmin):
    list_display = ('location', 'soil_type', 'pH', 'nitrogen', 'phosphorus', 'potassium', 'suitable_crops')
    search_fields = ('location', 'soil_type', 'suitable_crops')
