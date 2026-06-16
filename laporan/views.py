from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from whatsapp_gateway.services import send_fonnte_message
from .forms import LaporanHafalanForm
from .models import LaporanHafalan
from .services import build_laporan_hafalan, build_progress_chart, render_pesan_laporan
from django.contrib.auth.decorators import login_required 

@login_required
def report_list(request):
    laporan = LaporanHafalan.objects.select_related("santri").all()
    return render(request, "laporan/report_list.html", {"laporan": laporan})

@login_required
def report_create(request):
    if request.method == "POST":
        form = LaporanHafalanForm(request.POST)
        if form.is_valid():
            laporan = build_laporan_hafalan(
                santri=form.cleaned_data["santri"],
                periode_awal=form.cleaned_data["periode_awal"],
                periode_akhir=form.cleaned_data["periode_akhir"],
                catatan_perkembangan=form.cleaned_data["catatan_perkembangan"],
            )
            messages.success(request, "Laporan hafalan berhasil dibuat.")
            return redirect("laporan:detail", pk=laporan.pk)
    else:
        form = LaporanHafalanForm()
    return render(request, "laporan/report_form.html", {"form": form})
@login_required
def report_update(request, pk):

    laporan = get_object_or_404(
        LaporanHafalan,
        pk=pk
    )

    if request.method == "POST":

        form = LaporanHafalanForm(
            request.POST,
            instance=laporan
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Laporan berhasil diperbarui."
            )

            return redirect(
                "laporan:detail",
                pk=laporan.pk
            )

    else:

        form = LaporanHafalanForm(
            instance=laporan
        )

    return render(
        request,
        "laporan/report_form.html",
        {
            "form": form,
            "edit_mode": True
        }
    )
@login_required
def report_delete(request, pk):

    laporan = get_object_or_404(
        LaporanHafalan,
        pk=pk
    )

    if request.method == "POST":

        laporan.delete()

        messages.success(
            request,
            "Laporan berhasil dihapus."
        )

        return redirect("laporan:list")

    return render(
        request,
        "laporan/report_confirm_delete.html",
        {
            "laporan": laporan
        }
    )

def report_detail(request, pk):
    laporan = get_object_or_404(LaporanHafalan.objects.select_related("santri"), pk=pk)
    pesan = render_pesan_laporan(laporan)
    progress_chart, progress_status = build_progress_chart(
        laporan.santri,
        laporan.periode_awal,
        laporan.periode_akhir,
    )
    return render(
        request,
        "laporan/report_detail.html",
        {
            "laporan": laporan,
            "pesan": pesan,
            "progress_chart": progress_chart,
            "progress_status": progress_status,
        },
    )


def report_send(request, pk):
    laporan = get_object_or_404(LaporanHafalan.objects.select_related("santri"), pk=pk)
    pesan = render_pesan_laporan(laporan)
    log = send_fonnte_message(
        nomor_tujuan=laporan.santri.nomor_wa_orang_tua,
        pesan=pesan,
        laporan=laporan,
    )
    laporan.status_pengiriman = log.status
    laporan.save(update_fields=["status_pengiriman", "updated_at"])

    if log.status == "sent":
        messages.success(request, "Laporan berhasil dikirim melalui Fonnte.")
    elif log.status == "simulated":
        messages.info(request, "Mode simulasi aktif. Pesan dicatat tetapi belum dikirim ke WhatsApp.")
    else:
        messages.error(request, "Pengiriman laporan gagal. Periksa token Fonnte atau nomor tujuan.")

    return redirect("laporan:detail", pk=laporan.pk)

# Create your views here.
