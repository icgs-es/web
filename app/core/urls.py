from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("servicios/", views.services, name="services"),
    path("proyectos/", views.projects, name="projects"),
    path("sobre-icgs/", views.about, name="about"),
    path("contacto/", views.contact, name="contact"),
    path("privacidad/", views.privacidad, name="privacidad"),
    path("cookies/", views.cookies, name="cookies"),
    path("aviso-legal/", views.aviso_legal, name="aviso_legal"),
    path("soluciones/", views.soluciones, name="soluciones"),
    path("soluciones/ordix/", views.ordix, name="ordix"),
    path("soluciones/portal-intasa/", views.portal_intasa, name="portal_intasa"),
    path("proyectos/robotics-lab/", views.robotics_lab, name="robotics_lab"),
    path("proyectos/los-pedroches/", views.pedroches, name="pedroches"),
    # 301 redirect from old Robotics Lab URL
    path(
        "soluciones/robotics-lab/",
        RedirectView.as_view(url="/proyectos/robotics-lab/", permanent=True),
    ),
]
