from django.urls import path
from .views import list_bienes, retrieve_bien, create_bien_view, update_bien_ambiente, delete_bien_image, save_image_to_db_rest, delete_image_from_db, get_imagenes_by_inventario, update_bien_ambiente

urlpatterns = [
    path('bienes/', list_bienes, name='list_bienes'),
    path('bienes/<str:inventario>/', retrieve_bien, name='retrieve_bien'),
    path('bienes/create/', create_bien_view, name='create_bien'),
    path('bienes/<str:inventario>/update-ambiente/', update_bien_ambiente, name='update_bien_ambiente'),
    path('bienes/image/<int:image_id>/delete/', delete_bien_image, name='delete_bien_image'),
    path('api/image/<str:inventario>/upload/', save_image_to_db_rest, name='save_image_to_db_rest'),
    path('api/image/<str:inventario>/delete/', delete_image_from_db, name='delete_image_from_db'),
    path('api/image/<str:inventario>/list/', get_imagenes_by_inventario, name='get_imagenes_by_inventario'),
    path('api/image/<str:inventario>/update/', update_bien_ambiente, name='update_bien_ambiente'),
]


