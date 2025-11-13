from django.contrib import admin
from .models import Team, Activity, Workout, LeaderboardEntry


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'timestamp', 'distance')
    list_filter = ('activity_type',)
    search_fields = ('user__username',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'date', 'duration_seconds')
    search_fields = ('user__username', 'name')


@admin.register(LeaderboardEntry)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'points', 'rank', 'updated_at')
    search_fields = ('user__username',)
