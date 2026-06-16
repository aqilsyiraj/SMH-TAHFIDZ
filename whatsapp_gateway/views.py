from django.shortcuts import render
from .models import WhatsAppLog
from django.contrib.auth.decorators import login_required 
from accounts.decorators import admin_required
from django.contrib import messages
from django.shortcuts import (
    redirect,
    render,
)
from accounts.decorators import admin_required
from .forms import WhatsAppSettingForm
from .models import WhatsAppSetting

@login_required
@admin_required
def log_list(request):

    logs = WhatsAppLog.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "whatsapp_gateway/log_list.html",
        {
            "logs": logs
        }
    )
@login_required
@admin_required
def whatsapp_setting(request):

    setting, created = WhatsAppSetting.objects.get_or_create(
        pk=1,
        defaults={
            "token": "",
            "nomor_gateway": "",
        }
    )

    if request.method == "POST":

        form = WhatsAppSettingForm(
            request.POST,
            instance=setting
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Pengaturan WhatsApp berhasil disimpan."
            )

            return redirect(
                "whatsapp_gateway:setting"
            )

    else:

        form = WhatsAppSettingForm(
            instance=setting
        )

    return render(
        request,
        "whatsapp_gateway/setting.html",
        {
            "form": form
        }
    )


