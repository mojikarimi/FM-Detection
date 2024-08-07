from django.db import models


# Create your models here.


class Duc(models.Model):
    class Meta:
        verbose_name_plural = 'Documents For FMD'

    title = models.CharField(max_length=150, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title


class FilesPredicts(models.Model):
    class Meta:
        verbose_name_plural = 'Files Prediction'

    original_file = models.CharField(max_length=150, blank=True)
    original_file_url = models.TextField(blank=True)
    Prediction_file = models.CharField(max_length=150, blank=True)
    Prediction_file_url = models.TextField(blank=True)

    def __str__(self):
        return self.original_file
