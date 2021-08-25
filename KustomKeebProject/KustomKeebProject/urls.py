from django.contrib import admin
from django.urls import path, include

# when i want to import values from the settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# path('api/', include('base.urls')),


# viewing images uploaded from django
# static helps me add to  my  url patterns
