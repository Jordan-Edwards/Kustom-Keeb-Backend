from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views
from .views import UserViewSet


app_name = 'store'

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/<int:category_id>', views.ProductByCategoryList.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetails.as_view()),

]
