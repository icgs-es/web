from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path(
        "soluciones/robotics-lab/",
        TemplateView.as_view(template_name="core/robotics_lab.html"),
        name="robotics_lab",
    ),

    path("", views.home, name="home"),
    path("servicios/", views.services, name="services"),
    path("proyectos/", views.projects, name="projects"),
    path("sobre-icgs/", views.about, name="about"),
    path("contacto/", views.contact, name="contact"),
    path("privacidad/", views.privacidad, name="privacidad"),
    path("cookies/", views.cookies, name="cookies"),
    path("aviso-legal/", views.aviso_legal, name="aviso_legal"),
    path("soluciones/ordix/", TemplateView.as_view(template_name="core/ordix.html"), name="ordix"),
]
