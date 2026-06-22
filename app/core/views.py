from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Project, Lead, Screenshot, Solucion
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    soluciones = Solucion.objects.filter(is_active=True).order_by("order")
    return render(request, "core/home.html", {
        "services": Service.objects.filter(is_active=True).order_by("order")[:6],
        "soluciones": soluciones,
        "caso_real": soluciones.filter(destacado_en_home=True).first(),
        "enviado": request.GET.get("enviado") == "1",
        "form_error": request.GET.get("error") == "1",
    })


def services(request):
    return render(request, "core/services.html", {
        "services": Service.objects.filter(is_active=True).order_by("order"),
    })


def projects(request):
    return render(request, "core/projects.html", {
        "projects": Project.objects.filter(is_active=True).order_by("order"),
    })


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()
        origin = request.POST.get("origin", "home")

        if not name or not email or not message:
            if origin == "contact":
                return redirect("/contacto/?error=1")
            return redirect("/?error=1#contacto")

        Lead.objects.create(name=name, email=email, message=message)

        try:
            send_mail(
                subject=f"[ICGS] Nuevo contacto: {name}",
                message=(
                    f"Nuevo mensaje desde icgs.es\n\n"
                    f"Nombre: {name}\nEmail: {email}\n\nMensaje:\n{message}\n"
                ),
                from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None) or "no-reply@icgs.es",
                recipient_list=[getattr(settings, "CONTACT_NOTIFY_EMAIL", "ivan@icgs.es")],
                fail_silently=True,
            )
        except Exception:
            pass

        if origin == "contact":
            return redirect("/contacto/?enviado=1")
        return redirect("/?enviado=1#contacto")

    return render(request, "core/contact.html", {
        "enviado": request.GET.get("enviado") == "1",
        "form_error": request.GET.get("error") == "1",
    })


def soluciones(request):
    return render(request, "core/soluciones.html", {
        "soluciones": Solucion.objects.filter(is_active=True).order_by("order"),
    })


def ordix(request):
    return render(request, "core/ordix.html")


def robotics_lab(request):
    return render(request, "core/robotics_lab.html")


def portal_intasa(request):
    screenshots = Screenshot.objects.filter(page='portal_intasa', is_active=True).order_by('order')
    return render(request, "core/portal_intasa.html", {"screenshots": screenshots})


def pedroches(request):
    return render(request, "core/pedroches.html")


def privacidad(request):
    return render(request, "core/privacidad.html")

def cookies(request):
    return render(request, "core/cookies.html")

def aviso_legal(request):
    return render(request, "core/aviso_legal.html")
