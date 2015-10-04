from django.contrib import admin
from .models import VotingOption

class VotingOptionAdmin(admin.ModelAdmin):
  list_display = ('title', 'category', 'description', 'image')

admin.site.register(VotingOption, VotingOptionAdmin)
