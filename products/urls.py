from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('favorite/', views.favorite_view, name='favorite'),
    path('add-to-favorite/<int:product_id>/', views.add_to_favorite, name='add-to-favorite'),
    path('remove-from-favorite/<int:product_id>/', views.remove_from_favorite, name='remove-from-favorite'),
    path('add-review/<int:product_id>/', views.add_review, name='add_review'),
    path('edit-review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
]
