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
        "has_file",
    ]
    list_filter = ["is_critical", "is_active", "release_date"]
    search_fields = ["version", "release_notes"]
    readonly_fields = [
        "created_at",
        "updated_at",
        "checksum",
        "file_size",
        "download_url_display",
    ]

    fieldsets = (
        (
            "Version Information",
            {"fields": ("version", "build_number", "minimum_version")},
        ),
        (
            "Download Information",
            {
                "fields": (
                    "download_file",
                    "download_url_display",
                    "checksum",
                    "file_size",
                )
            },
        ),
        (
            "Release Information",
            {"fields": ("release_notes", "release_date", "is_critical", "is_active")},
        ),
        ("Metadata", {"fields": ("created_at", "updated_at"), "classes": ["collapse"]}),
    )

    def has_file(self, obj):
        return bool(obj.download_file)

    has_file.boolean = True
    has_file.short_description = "Has File"

    def download_url_display(self, obj):
        return obj.download_url

    download_url_display.short_description = "Download URL"
