"""Cards models admin."""

# Django
from django.contrib import admin

# Model
from .models import WhiteCard, BlackCard

@admin.register(WhiteCard)
class WhiteCardAdmin(admin.ModelAdmin):
    pass

@admin.register(BlackCard)
class BlackCardAdmin(admin.ModelAdmin):
    pass

