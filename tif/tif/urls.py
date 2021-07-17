from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('kudos.urls')),
    path('admin/', admin.site.urls),
]
