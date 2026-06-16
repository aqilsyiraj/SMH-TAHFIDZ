# SIMTAHFIDZ-ZBT

Aplikasi web Django untuk rekapitulasi hafalan santri dan pelaporan ke orang tua melalui WhatsApp Gateway Fonnte.

## Fitur

- Dashboard jumlah santri, setoran, laporan, dan log WhatsApp.
- Master data santri dan orang tua.
- Input setoran hafalan: ziyadah, murajaah, dan tasmi.
- Generate laporan hafalan berdasarkan periode.
- Preview pesan laporan.
- Kirim atau simulasi pengiriman WhatsApp melalui Fonnte.

## Menjalankan Aplikasi

```powershell
.\.venv\Scripts\activate
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Buka:

```text
http://127.0.0.1:8000/
```

## Konfigurasi Fonnte

Salin `.env.example` menjadi `.env`, lalu isi token Fonnte:

```env
FONNTE_TOKEN=token_dari_dashboard_fonnte
FONNTE_SIMULATION_MODE=False
```

Saat `FONNTE_SIMULATION_MODE=True`, aplikasi hanya menyimpan log pesan tanpa mengirim WhatsApp sungguhan.
