from django.contrib import admin

from .models import SetoranHafalan


@admin.register(SetoranHafalan)
class SetoranHafalanAdmin(admin.ModelAdmin):
    list_display = ("tanggal", "santri", "jenis_setoran", "kategori_juz", "halaman_awal", "halaman_akhir", "kualitas",)
    list_filter = ("jenis_setoran", "kategori_juz", "kualitas", "tanggal")
    search_fields = ("santri__nama", "santri__nis", "catatan")
    date_hierarchy = "tanggal"

# Register your models here.
