
from django.db import models


class StatusChoices(models.TextChoices):
    IN_PROCESS = "IN PROCESS"
    DONE = "DONE"
    FAILED = "FAILED"