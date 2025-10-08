from django.urls import path
from .views import UpdateCheckView, UpdateStatsView

urlpatterns = [
    path("updates/check/", UpdateCheckView.as_view(), name="update-check"),
    path("updates/stats/", UpdateStatsView.as_view(), name="update-stats"),
]
