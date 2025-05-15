from django.urls import path
from .views import list_bienes, retrieve_bien, create_bien_view, update_bien_ambiente, delete_bien_image

urlpatterns = [
    path('bienes/', list_bienes, name='list_bienes'),
    path('bienes/<str:inventario>/', retrieve_bien, name='retrieve_bien'),
    path('bienes/create/', create_bien_view, name='create_bien'),
    path('bienes/<str:inventario>/update-ambiente/', update_bien_ambiente, name='update_bien_ambiente'),
    path('bienes/image/<int:image_id>/delete/', delete_bien_image, name='delete_bien_image'),
]


