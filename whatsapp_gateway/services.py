import requests

from django.conf import settings

from django.utils import timezone

from .models import (
    WhatsAppLog,
    WhatsAppSetting,
)


def send_fonnte_message(
    nomor_tujuan,
    pesan,
    laporan=None
):

    log = WhatsAppLog.objects.create(

        laporan=laporan,

        nomor_tujuan=nomor_tujuan,

        pesan=pesan,

        status="pending",
    )

    # =========================
    # AMBIL PENGATURAN DARI DATABASE
    # =========================

    setting = WhatsAppSetting.objects.first()

    # jika belum ada pengaturan

    if not setting:

        log.status = "failed"

        log.response = {
            "error": "Pengaturan WhatsApp belum dibuat."
        }

        log.save()

        return log

    token = setting.token

    simulation_mode = setting.simulation_mode

    country_code = setting.country_code

    # =========================
    # MODE SIMULASI
    # =========================

    if simulation_mode or not token:

        log.status = "simulated"

        log.response = {
            "message":
            "Mode simulasi aktif atau token belum diisi."
        }

        log.sent_at = timezone.now()

        log.save()

        return log

    # =========================
    # REQUEST FONNTE
    # =========================

    headers = {
        "Authorization": token
    }

    payload = {

        "target": nomor_tujuan,

        "message": pesan,

        "countryCode": country_code,
    }

    try:

        response = requests.post(

            settings.FONNTE_API_URL,

            headers=headers,

            data=payload,

            timeout=15,
        )

        result = response.json()

        log.response = result

        log.status = (
            "sent"
            if result.get("status") is True
            else "failed"
        )

        log.sent_at = timezone.now()

        log.save()

    except requests.RequestException as error:

        log.status = "failed"

        log.response = {
            "error": str(error)
        }

        log.save()

    return log