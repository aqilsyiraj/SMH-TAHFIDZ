from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .forms import SetoranHafalanForm
from .models import SetoranHafalan
from django.contrib.auth.decorators import login_required 

@login_required
def setoran_list(request):
    setoran = SetoranHafalan.objects.select_related("santri").all()
    return render(request, "hafalan/setoran_list.html", {"setoran": setoran})

@login_required
def setoran_create(request):
    if request.method == "POST":
        form = SetoranHafalanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Setoran hafalan berhasil disimpan.")
            return redirect("hafalan:list")
    else:
        form = SetoranHafalanForm()
    return render(request, "hafalan/setoran_form.html", {"form": form})
@login_required
def setoran_update(request, pk):

    setoran = SetoranHafalan.objects.get(pk=pk)

    if request.method == "POST":

        form = SetoranHafalanForm(
            request.POST,
            instance=setoran
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Data setoran berhasil diperbarui."
            )

            return redirect("hafalan:list")

    else:

        form = SetoranHafalanForm(instance=setoran)

    return render(
        request,
        "hafalan/setoran_form.html",
        {
            "form": form,
            "edit_mode": True
        }
    )
@login_required
def setoran_delete(request, pk):

    setoran = get_object_or_404(
        SetoranHafalan,
        pk=pk
    )

    if request.method == "POST":

        setoran.delete()

        return redirect("hafalan:list")

    return render(
        request,
        "hafalan/setoran_confirm_delete.html",
        {
            "setoran": setoran
        }
    )
