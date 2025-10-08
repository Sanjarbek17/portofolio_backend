from django.contrib import admin
from .models import ApplicationVersion


@admin.register(ApplicationVersion)
class ApplicationVersionAdmin(admin.ModelAdmin):
    list_display = [
        "version",
        "build_number",
        "is_critical",
        "is_active",
        "release_date",
    ]
    list_filter = ["is_critical", "is_active", "release_date"]
    search_fields = ["version", "release_notes"]
    readonly_fields = ["created_at", "updated_at", "checksum"]

    fieldsets = (
        (
            "Version Information",
            {"fields": ("version", "build_number", "minimum_version")},
        ),
        ("Download Information", {"fields": ("download_url", "checksum", "file_size")}),
        (
            "Release Information",
            {"fields": ("release_notes", "release_date", "is_critical", "is_active")},
        ),
        ("Metadata", {"fields": ("created_at", "updated_at"), "classes": ["collapse"]}),
    )
