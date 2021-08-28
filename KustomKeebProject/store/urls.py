from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('category/<int:category_id>', views.ProductByCategoryList.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetails.as_view()),

    # path('product/<int:category_id>/', views.ProductList.as_view()),
]
