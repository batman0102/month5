
from django.contrib import admin
from django.urls import path, include
from product import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.products_list_api_view),
    path('api/v1/products/<int:id>/', views.products_detail_api_view),
    path('api/v1/reviews/', views.reviews_list_api_view),
    path('api/v1/reviews/<int:id>', views.review_api_view),
    path('api/v1/categories/', views.categories_list_api_view),
    path('api/v1/categories/<int:id>', views.category_api_view),
    path('api/v1/products/reviews/', views.products_reviews_api_view),
    path('api/v1/users/registration/', user_views.registration_api_view),
    path('api/v1/users/authorization/', user_views.authorization_api_view),
    path('api/v1/users/confirm/', user_views.confirm_registration_api_view),
]
