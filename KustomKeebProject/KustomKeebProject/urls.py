from django.contrib import admin
from django.urls import path, include

# when i want to import values from the settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('base.urls')),
    path('api/products/', include('base.urls.product_urls')),
    path('api/users/', include('base.urls.user_urls')),
    path('api/orders/', include('base.urls.order_urls'))
]


# viewing images uploaded from django
# static helps me add to  my  url patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
