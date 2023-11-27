from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from metrics import views
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main_index, name="main_index"),
    path("api/timestamps", views.timeStamps),
    path("analysis/", views.analysis_index, name='analysis_index'),
    path("classification/", views.classification_index,
         name='classification_index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
