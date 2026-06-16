from django.db import models


class Santri(models.Model):
    JENIS_KELAMIN_CHOICES = [
        ("L", "Laki-laki"),
        ("P", "Perempuan"),
    ]

    nama = models.CharField(max_length=150)
    nis = models.CharField("NIS", max_length=50, unique=True)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES)
    tanggal_lahir = models.DateField(null=True, blank=True)
    ustadz_pembina = models.CharField(max_length=150, default="Belum diisi")
    nama_orang_tua = models.CharField(max_length=150)
    nomor_wa_orang_tua = models.CharField("Nomor WhatsApp Orang Tua", max_length=20)
    alamat = models.TextField(blank=True)
    aktif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Santri"
        verbose_name_plural = "Santri"
        ordering = ["nama"]

    def __str__(self):
        return f"{self.nama} ({self.nis})"

# Create your models here.
