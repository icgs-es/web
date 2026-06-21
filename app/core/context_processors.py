from .models import SiteSettings

def site_settings(request):
    obj = SiteSettings.objects.first()
    if obj is None:
        obj = SiteSettings(site_name="ICGS")
    return {"settings": obj}
