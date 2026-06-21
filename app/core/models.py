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
    summary = models.CharField(max_length=240, blank=True)
    stack = models.CharField(max_length=120, blank=True)
    url = models.URLField(blank=True)
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

