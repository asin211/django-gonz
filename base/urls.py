"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# for static files and settings from settings (set this 2 imports below for images and install pillow)
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = "GoNZ Admin"
admin.site.site_title = "GoNZ Admin Portal"
admin.site.index_title = "Welcome to GoNZ Portal"


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
]

# add this from images uploading in static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# for deployment (not required)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
