from django.contrib import admin

from .models import LaporanHafalan


@admin.register(LaporanHafalan)
class LaporanHafalanAdmin(admin.ModelAdmin):
    list_display = ("santri", "periode_awal", "periode_akhir", "total_setoran", "rata_rata_setoran_harian", "kategori_juz_terakhir", "status_pengiriman")
    list_filter = ("status_pengiriman", "periode_awal", "periode_akhir")
    search_fields = ("santri__nama", "santri__nis", "catatan_perkembangan")

# Register your models here.
