from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle
from django.http import Http404
from .models import ApplicationVersion
import logging

logger = logging.getLogger(__name__)


class UpdateCheckView(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        """Check for available updates"""
        try:
            # Get current version from headers
            current_version = request.META.get("HTTP_X_CURRENT_VERSION", "0.0.0")
            current_build = int(request.META.get("HTTP_X_CURRENT_BUILD", 0))
            user_agent = request.META.get("HTTP_USER_AGENT", "")

            logger.info(
                f"Update check: {user_agent} - Current: {current_version} (Build {current_build})"
            )

            # Get the latest active version
            try:
                latest_version = ApplicationVersion.objects.filter(
                    is_active=True
                ).first()
            except ApplicationVersion.DoesNotExist:
                logger.warning("No active versions found")
                return Response(status=status.HTTP_204_NO_CONTENT)

            if not latest_version:
                return Response(status=status.HTTP_204_NO_CONTENT)

            # Check if update is available
            if latest_version.is_newer_than(current_version, current_build):
                update_data = {
                    "version": latest_version.version,
                    "buildNumber": latest_version.build_number,
                    "downloadUrl": latest_version.download_url,
                    "checksum": latest_version.checksum,
                    "fileSize": latest_version.file_size,
                    "releaseNotes": latest_version.release_notes,
                    "isCritical": latest_version.is_critical,
                    "minimumVersion": latest_version.minimum_version,
                    "releaseDate": latest_version.release_date.isoformat(),
                }

                logger.info(
                    f"Update available: {latest_version.version} for client {current_version}"
                )
                return Response(update_data, status=status.HTTP_200_OK)
            else:
                logger.info(f"Client {current_version} is up to date")
                return Response(status=status.HTTP_204_NO_CONTENT)

        except ValueError as e:
            logger.error(f"Invalid build number: {e}")
            return Response(
                {"error": "Invalid build number"}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Update check error: {e}")
            return Response(
                {"error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UpdateStatsView(APIView):
    """Optional: View for update statistics"""

    def get(self, request):
        """Get update statistics"""
        versions = ApplicationVersion.objects.filter(is_active=True)
        return Response(
            {
                "total_versions": versions.count(),
                "latest_version": (
                    versions.first().version if versions.exists() else None
                ),
                "latest_build": (
                    versions.first().build_number if versions.exists() else None
                ),
            }
        )
