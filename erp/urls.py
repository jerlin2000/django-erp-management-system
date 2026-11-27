from django.contrib import admin
from django.urls import path
from django.views.i18n import set_language

from inventory.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("language/", set_language, name="set_language"),
    path("", dashboard, name="dashboard"),
]
