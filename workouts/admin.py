from django.contrib import admin
from .models import Exercise, Plan, WorkoutSession, WorkoutSet

admin.site.register(Exercise)
admin.site.register(Plan)
admin.site.register(WorkoutSession)
admin.site.register(WorkoutSet)