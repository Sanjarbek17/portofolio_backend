from django.db import models
from django.utils import timezone
import hashlib
import os


class ApplicationVersion(models.Model):
    version = models.CharField(max_length=20)
    build_number = models.IntegerField()
    download_url = models.URLField()
    checksum = models.CharField(max_length=64)
    file_size = models.BigIntegerField()
    release_notes = models.TextField()
    is_critical = models.BooleanField(default=False)
    minimum_version = models.CharField(max_length=20, blank=True, null=True)
    release_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-build_number"]
        unique_together = ["version", "build_number"]

    def __str__(self):
        return f"SenseLite v{self.version} (Build {self.build_number})"

    def save(self, *args, **kwargs):
        # Auto-calculate checksum if file exists
        if self.download_url and not self.checksum:
            self.checksum = self.calculate_checksum()
        super().save(*args, **kwargs)

    def calculate_checksum(self):
        """Calculate SHA256 checksum of the file"""
        try:
            # This is a simple example - in production, you'd want to
            # calculate the checksum of the actual file
            return "sha256:placeholder-checksum"
        except Exception:
            return ""

    def is_newer_than(self, current_version, current_build):
        """Check if this version is newer than the provided version"""
        current_parts = [int(x) for x in current_version.split(".")]
        this_parts = [int(x) for x in self.version.split(".")]

        # Pad with zeros if needed
        max_len = max(len(current_parts), len(this_parts))
        current_parts.extend([0] * (max_len - len(current_parts)))
        this_parts.extend([0] * (max_len - len(this_parts)))

        # Compare version parts
        for current, this in zip(current_parts, this_parts):
            if this > current:
                return True
            elif this < current:
                return False

        # If versions are equal, compare build numbers
        return self.build_number > current_build
