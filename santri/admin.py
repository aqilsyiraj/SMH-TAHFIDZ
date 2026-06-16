from django.contrib import admin

from .models import Santri


@admin.register(Santri)
class SantriAdmin(admin.ModelAdmin):
    list_display = ("nama", "nis", "jenis_kelamin", "ustadz_pembina", "nama_orang_tua", "nomor_wa_orang_tua", "aktif")
    list_filter = ("aktif", "jenis_kelamin", "ustadz_pembina")
    search_fields = ("nama", "nis", "nama_orang_tua", "nomor_wa_orang_tua")

# Register your models here.
