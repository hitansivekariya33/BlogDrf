from django.urls import path
from .views import BlogListView, BlogDetailView, AuthorListView, AuthorDeatilView, RegisterView, LoginView, LogoutView
from rest_framework_simplejwt.views  import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('blogs/', BlogListView.as_view(), name='bloglist'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blogdetail'),
    path('author/', AuthorListView.as_view(), name='authorlist'),
    path('author/<int:pk>/', AuthorDeatilView.as_view(), name='authordetail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
