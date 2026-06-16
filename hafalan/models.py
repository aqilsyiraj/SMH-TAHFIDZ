from django.db import models


class SetoranHafalan(models.Model):
    JENIS_SETORAN_CHOICES = [
        ("ziyadah", "Ziyadah"),
        ("murajaah", "Murajaah"),
    ]

    KUALITAS_CHOICES = [
        ("sangat_baik", "Sangat Baik"),
        ("baik", "Baik"),
        ("cukup", "Cukup"),
        ("perlu_bimbingan", "Perlu Bimbingan"),
    ]

    KATEGORI_JUZ_CHOICES = [
        ("juz_1_5", "1-5 Juz"),
        ("juz_1_10", "1-10 Juz"),
        ("juz_1_15", "1-15 Juz"),
        ("juz_1_20", "1-20 Juz"),
        ("juz_1_25", "1-25 Juz"),
        ("juz_1_30", "1-30 Juz"),
    ]

    KATEGORI_JUZ_MAX = {
        "juz_1_5": 5,
        "juz_1_10": 10,
        "juz_1_15": 15,
        "juz_1_20": 20,
        "juz_1_25": 25,
        "juz_1_30": 30,
    }

    santri = models.ForeignKey(
        "santri.Santri",
        on_delete=models.CASCADE,
        related_name="setoran_hafalan",
    )
    tanggal = models.DateField()
    jenis_setoran = models.CharField(max_length=20, choices=JENIS_SETORAN_CHOICES)
    kategori_juz = models.CharField(max_length=20, choices=KATEGORI_JUZ_CHOICES, default="juz_1_5")
    surah = models.CharField(max_length=100)
    halaman_awal = models.PositiveIntegerField()
    halaman_akhir = models.PositiveIntegerField()
    kualitas = models.CharField(max_length=30, choices=KUALITAS_CHOICES, default="baik")
    catatan = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Setoran Hafalan"
        verbose_name_plural = "Setoran Hafalan"
        ordering = ["-tanggal", "santri__nama"]

    @property
    def rentang_halaman(self): 
        f"{self.surah} "
        return f"Halaman {self.halaman_awal}-{self.halaman_akhir}"

    @property
    def kategori_juz_maks(self):
        return self.KATEGORI_JUZ_MAX.get(self.kategori_juz, 0)

    def __str__(self):
        return f"{self.santri.nama} - {self.rentang_halaman}"

# Create your models here.
