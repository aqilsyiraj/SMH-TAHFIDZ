from django.db import models


class Halaqah(models.Model):
    nama = models.CharField(max_length=120, unique=True)
    ustadz_pembimbing = models.CharField(max_length=150)
    target_hafalan = models.CharField(max_length=120, blank=True)
    keterangan = models.TextField(blank=True)
    aktif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Halaqah"
        verbose_name_plural = "Halaqah"
        ordering = ["nama"]

    def __str__(self):
        return self.nama

# Create your models here.
