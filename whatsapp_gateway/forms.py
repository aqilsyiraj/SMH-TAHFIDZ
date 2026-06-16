from django import forms

from .models import WhatsAppSetting


class WhatsAppSettingForm(forms.ModelForm):

    class Meta:

        model = WhatsAppSetting

        fields = [

            "nama_instansi",
            "token",
            "nomor_gateway",
            "country_code",
            "simulation_mode",

        ]

        widgets = {

            "token": forms.TextInput(
                attrs={
                    "class": "modern-input"
                }
            ),

            "nomor_gateway": forms.TextInput(
                attrs={
                    "class": "modern-input"
                }
            ),

        }