from django.conf import settings
from django.contrib.gis.db import models


class Spot(models.Model):
    class Category(models.TextChoices):
        RESTAURANT = "restaurant", "Restaurant"
        CAFE = "cafe", "Café"
        LANDMARK = "landmark", "Landmark"
        VIEWPOINT = "viewpoint", "Viewpoint"
        HIKING_TRAIL = "hiking_trail", "Hiking Trail"
        OTHER = "other", "Other"

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=50,
        choices=Category.choices,
        default=Category.OTHER,
    )
    location = models.PointField(srid=4326)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="spots",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name
