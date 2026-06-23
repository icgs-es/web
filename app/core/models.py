from django.db import models
from django.utils.text import slugify

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=120, default="ICGS")
    meta_description = models.CharField(max_length=200, blank=True, default="Servicios tecnológicos, automatización e infraestructura.")

    hero_title = models.CharField(max_length=160, blank=True, default="Infraestructura y automatización para tu negocio")
    hero_subtitle = models.TextField(blank=True, default="Diseño y despliego soluciones estables con Docker, Cloudflare y desarrollo Django/Odoo.")

    primary_cta_text = models.CharField(max_length=80, blank=True, default="Solicitar propuesta")
    primary_cta_url = models.CharField(max_length=200, blank=True, default="/contacto/")
    secondary_cta_text = models.CharField(max_length=80, blank=True, default="Ver servicios")
    secondary_cta_url = models.CharField(max_length=200, blank=True, default="/servicios/")

    email = models.EmailField(blank=True, default="ivan@icgs.es")
    footer_text = models.CharField(max_length=200, blank=True, default="Infraestructura, automatización y desarrollo para empresas.")
    about_text = models.TextField(blank=True, default="")

    # Branding (requiere MEDIA)
    logo = models.ImageField(upload_to="brand/", blank=True, null=True)
    favicon = models.ImageField(upload_to="brand/", blank=True, null=True)
    og_image = models.ImageField(upload_to="brand/", blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ajustes del sitio"
        verbose_name_plural = "Ajustes del sitio"

    def __str__(self):
        return "Ajustes del sitio"


class Service(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    summary = models.CharField(max_length=240, blank=True)
    content = models.TextField(blank=True)

    # Campos de tarjeta rica
    descripcion = models.TextField(blank=True, help_text="Párrafo principal de presentación del servicio")
    incluye = models.TextField(blank=True, help_text="Lista de lo que incluye — un elemento por línea")
    precio_badge = models.CharField(max_length=60, blank=True, help_text="Ej: Desde 60 €/mes")
    precio_detalle = models.TextField(blank=True, help_text="Desglose de precios — una línea por tramo")
    cta_texto = models.CharField(max_length=80, blank=True, default='Consultar →')
    cta_url = models.CharField(max_length=200, blank=True, default='/contacto/')
    icono_key = models.CharField(max_length=30, blank=True,
        help_text="shield | server | code | gear")

    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:160]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    cat = models.CharField(max_length=120, blank=True, help_text="Etiqueta sol-cat, ej: 'ICGS ROBOTICS LAB · Nexo Operativo'")
    titulo_card = models.CharField(max_length=200, blank=True, help_text="Titular descriptivo del card")
    summary = models.CharField(max_length=240, blank=True)
    badge_clase = models.CharField(max_length=30, default='badge-dev', help_text="badge-live o badge-dev")
    badge_texto = models.CharField(max_length=60, blank=True)
    stack = models.CharField(max_length=120, blank=True)
    url = models.URLField(blank=True)
    url_detalle = models.CharField(max_length=200, blank=True, help_text="URL de la página de detalle, ej: /proyectos/robotics-lab/")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:160]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Solucion(models.Model):
    slug = models.SlugField(max_length=80, unique=True)
    nombre = models.CharField(max_length=120)

    # Campos de tarjeta (home #soluciones + índice /soluciones/)
    cat = models.CharField(max_length=120, blank=True, help_text="Etiqueta sol-cat, ej: 'Inmobiliario · Oportunidades'")
    titulo_card = models.CharField(max_length=200, blank=True, help_text="Titular descriptivo del sol-card")
    badge_clase = models.CharField(max_length=30, default='badge-dev', help_text="badge-live o badge-dev")
    badge_texto = models.CharField(max_length=60, blank=True, help_text="Texto del badge, ej: 'En producción'")
    descripcion_card = models.TextField(blank=True, help_text="Descripción corta para la tarjeta")
    icono_static = models.CharField(max_length=100, blank=True, help_text="Ruta relativa a static/, ej: img/icgs/ordix-mark.png")

    # Campos de la sección proof (caso real) en home
    descripcion_home = models.TextField(blank=True, help_text="Texto largo para la sección 'Caso real' de la home")
    imagen_home = models.ImageField(upload_to='soluciones/', blank=True, null=True)
    pie_imagen = models.CharField(max_length=120, blank=True)
    destacado_en_home = models.BooleanField(default=False)

    url_detalle = models.CharField(max_length=200)
    texto_cta = models.CharField(max_length=80, default='Ver solución →')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ['order']
        verbose_name = 'Solución'
        verbose_name_plural = 'Soluciones'

    def __str__(self):
        return self.nombre


class Screenshot(models.Model):
    PAGE_CHOICES = [
        ('portal_intasa', 'Portal INTASA'),
        ('ordix', 'ORDIX CORE'),
        ('robotics', 'Robotics Lab'),
    ]
    page = models.CharField(max_length=40, choices=PAGE_CHOICES, default='portal_intasa')
    image = models.ImageField(upload_to='screenshots/')
    caption = models.CharField(max_length=120, blank=True)
    order = models.PositiveIntegerField(default=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['page', 'order']
        verbose_name = 'Captura de pantalla'
        verbose_name_plural = 'Capturas de pantalla'

    def __str__(self):
        return f"{self.get_page_display()} · {self.caption or f'#{self.order}'}"


class Lead(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=160, blank=True)
    message = models.TextField()
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Lead (contacto)"
        verbose_name_plural = "Leads (contactos)"

    def __str__(self):
        return f"{self.email} · {self.subject or 'Contacto'}"

