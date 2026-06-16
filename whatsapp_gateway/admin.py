from django.contrib import admin

from .models import (
    WhatsAppLog,
    WhatsAppSetting,
)

@admin.register(WhatsAppLog)
class WhatsAppLogAdmin(admin.ModelAdmin):
    list_display = ("nomor_tujuan", "status", "laporan", "created_at", "sent_at")
    list_filter = ("status", "created_at")
    search_fields = ("nomor_tujuan", "pesan")
    readonly_fields = ("response", "created_at", "sent_at")

admin.site.register(WhatsAppSetting)
