from django.db import models
from django.utils import timezone
import hashlib
import os


class ApplicationVersion(models.Model):
    version = models.CharField(max_length=20)
    build_number = models.IntegerField()
    download_file = models.FileField(upload_to="updates/", blank=True, null=True)
    checksum = models.CharField(max_length=64, blank=True)
    file_size = models.BigIntegerField(blank=True, null=True)
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

    @property
    def download_url(self):
        """Get the download URL for the file"""
        if self.download_file:
            return self.download_file.url
        return None

    def save(self, *args, **kwargs):
        # Auto-calculate file size and checksum if file exists
        if self.download_file:
            if not self.file_size:
                self.file_size = self.download_file.size
            if not self.checksum:
                self.checksum = self.calculate_checksum()
        super().save(*args, **kwargs)

    def calculate_checksum(self):
        """Calculate SHA256 checksum of the file"""
        if not self.download_file:
            return ""

        try:
            import hashlib

            hash_sha256 = hashlib.sha256()

            # Read file in chunks to handle large files
            self.download_file.seek(0)
            for chunk in iter(lambda: self.download_file.read(4096), b""):
                hash_sha256.update(chunk)
            self.download_file.seek(0)  # Reset file pointer

            return f"sha256:{hash_sha256.hexdigest()}"
        except Exception as e:
            return f"sha256:error-{str(e)[:20]}"

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
