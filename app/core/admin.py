from django.contrib import admin
from .models import SiteSettings, Service, Project, Lead, Screenshot, Solucion

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("General", {"fields": ("site_name", "meta_description", "email")}),
        ("Hero", {"fields": ("hero_title", "hero_subtitle")}),
        ("CTAs", {"fields": ("primary_cta_text", "primary_cta_url", "secondary_cta_text", "secondary_cta_url")}),
        ("Textos", {"fields": ("footer_text", "about_text")}),
        ("Branding (Media)", {"fields": ("logo", "favicon", "og_image")}),
    )

    def has_add_permission(self, request):
        # Solo 1 registro
        return not SiteSettings.objects.exists()

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order", "title")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "badge_texto", "is_active", "order")
    list_filter = ("badge_clase", "is_active")
    list_editable = ("is_active", "order")
    search_fields = ("title", "summary", "cat")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order", "title")
    fieldsets = (
        ("Identidad", {"fields": ("title", "slug", "url_detalle", "url", "is_active", "order")}),
        ("Tarjeta (índice /proyectos/)", {"fields": ("cat", "titulo_card", "badge_clase", "badge_texto", "summary")}),
    )
    
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "email",
        "subject",
        "is_processed",
    )

    list_filter = (
        "is_processed",
        "created_at",
    )

    search_fields = (
        "email",
        "subject",
        "message",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "created_at",
        "email",
        "subject",
        "message",
    )

    fieldsets = (
        ("Contacto", {
            "fields": ("email", "subject", "created_at"),
        }),
        ("Mensaje", {
            "fields": ("message",),
        }),
        ("Gestión", {
            "fields": ("is_processed",),
        }),
    )

    actions = ["marcar_como_procesado"]

    @admin.action(description="Marcar como procesado")
    def marcar_como_procesado(self, request, queryset):
        queryset.update(is_processed=True)


@admin.register(Solucion)
class SolucionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "badge_texto", "destacado_en_home", "is_active", "order")
    list_filter = ("badge_clase", "destacado_en_home", "is_active")
    list_editable = ("destacado_en_home", "is_active", "order")
    ordering = ("order",)
    fieldsets = (
        ("Identidad", {"fields": ("slug", "nombre", "url_detalle", "texto_cta", "is_active", "order")}),
        ("Tarjeta (home + índice)", {"fields": ("cat", "titulo_card", "badge_clase", "badge_texto", "descripcion_card", "icono_static")}),
        ("Sección 'Caso real' (home)", {"fields": ("descripcion_home", "imagen_home", "pie_imagen", "destacado_en_home")}),
    )


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ("page", "caption", "order", "is_active")
    list_filter = ("page", "is_active")
    ordering = ("page", "order")
    list_editable = ("order", "is_active")

