from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from metrics import views


urlpatterns = [
     path("admin/", admin.site.urls),
    path("", views.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
