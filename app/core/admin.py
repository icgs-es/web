from django.contrib import admin
from .models import SiteSettings, Service, Project, Lead

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
    list_display = ("title", "stack", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("title", "summary", "stack")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order", "title")
    
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

