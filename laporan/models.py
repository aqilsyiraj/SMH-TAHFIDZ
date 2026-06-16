from django.db import models


class LaporanHafalan(models.Model):
    STATUS_PENGIRIMAN_CHOICES = [
        ("belum_dikirim", "Belum Dikirim"),
        ("simulated", "Simulasi"),
        ("sent", "Terkirim"),
        ("failed", "Gagal"),
    ]

    santri = models.ForeignKey(
        "santri.Santri",
        on_delete=models.CASCADE,
        related_name="laporan_hafalan",
    )
    periode_awal = models.DateField()
    periode_akhir = models.DateField()
    total_setoran = models.PositiveIntegerField(default=0)
    rata_rata_setoran_harian = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    hafalan_terakhir = models.CharField(max_length=200, blank=True)
    kategori_juz_terakhir = models.CharField(max_length=50, blank=True)
    catatan_perkembangan = models.TextField(blank=True)
    status_pengiriman = models.CharField(
        max_length=20,
        choices=STATUS_PENGIRIMAN_CHOICES,
        default="belum_dikirim",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Laporan Hafalan"
        verbose_name_plural = "Laporan Hafalan"
        ordering = ["-periode_akhir", "santri__nama"]

    def __str__(self):
        return f"Laporan {self.santri.nama} ({self.periode_awal} - {self.periode_akhir})"

# Create your models here.
