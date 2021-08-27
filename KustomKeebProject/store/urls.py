from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('product/', views.ProductList.as_view()),
    # path('product/<int:category_id>/', views.ProductList.as_view()),
]

