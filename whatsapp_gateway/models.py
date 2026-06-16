from django.db import models


class WhatsAppLog(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("simulated", "Simulasi"),
        ("sent", "Terkirim"),
        ("failed", "Gagal"),
    ]

    laporan = models.ForeignKey(
        "laporan.LaporanHafalan",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="whatsapp_logs",
    )
    nomor_tujuan = models.CharField(max_length=20)
    pesan = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    response = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Log WhatsApp"
        verbose_name_plural = "Log WhatsApp"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.nomor_tujuan} - {self.status}"

class WhatsAppSetting(models.Model):

    nama_instansi = models.CharField(
        max_length=200,
        default="SMHTAHFIDZ-ZBT"
    )

    token = models.CharField(
        max_length=255
    )

    nomor_gateway = models.CharField(
        max_length=20
    )

    country_code = models.CharField(
        max_length=5,
        default="62"
    )

    simulation_mode = models.BooleanField(
        default=False
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.nama_instansi