from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ChurchStructure/', include('FRNChurchStructure.urls')),
    path('api/', include('FRNChurchStructure.api.urls')),
]
