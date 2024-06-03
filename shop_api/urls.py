
from django.contrib import admin
from django.urls import path, include
from product import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.ProductsCreateListAPIView.as_view()),
    path('api/v1/products/<int:id>/', views.ProductItemListApi.as_view()),
    path('api/v1/reviews/', views.ReviewsCreateListAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewItemListApi.as_view()),
    path('api/v1/categories/', views.CategoriesCreateListAPIView.as_view()),
    path('api/v1/categories/<int:id>/', views.CategoryItemListApi.as_view()),
    path('api/v1/products/reviews/', views.ProductsReviewsAPIView.as_view()),
    path('api/v1/users/registration/', user_views.RegistrationAPIView.as_view()),
    path('api/v1/users/authorization/', user_views.AuthorizationAPIView.as_view()),
    path('api/v1/users/confirm/', user_views.ConfirmRegistrationAPIView.as_view()),
]
