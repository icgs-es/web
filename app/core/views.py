# app/core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Project, Lead
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request, "core/home.html", {
        "services": Service.objects.filter(is_active=True).order_by("order")[:6],
        "projects": Project.objects.filter(is_active=True).order_by("order")[:6],
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
        company = request.POST.get("company", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(request, "Rellena nombre, email y mensaje.")
        else:
            Lead.objects.create(
                name=name,
                email=email,
                company=company,
                message=message,
                source="icgs.es",
            )
            # Email de notificación (si está configurado)
            try:
                subject = f"[ICGS] Nuevo contacto: {name}"
                body = (
                    f"Nuevo mensaje desde icgs.es\n\n"
                    f"Nombre: {name}\n"
                    f"Email: {email}\n"
                    f"Empresa: {company or '-'}\n\n"
                    f"Mensaje:\n{message}\n"
                )

                send_mail(
                    subject=subject,
                    message=body,
                    from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None) or "no-reply@icgs.es",
                    recipient_list=[getattr(settings, "CONTACT_NOTIFY_EMAIL", "ivan@icgs.es")],
                    fail_silently=False,
                )
            except Exception:
                # No bloqueamos el envío del formulario si falla el correo
                pass

            messages.success(request, "Mensaje enviado. Te responderé lo antes posible.")
            return redirect("contact")

    return render(request, "core/contact.html")

def privacidad(request):
    return render(request, "core/privacidad.html")

def cookies(request):
    return render(request, "core/cookies.html")

def aviso_legal(request):
    return render(request, "core/aviso_legal.html")

