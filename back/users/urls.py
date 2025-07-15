from django.urls import path
from .views import SignupView, LoginView, UserListCreateView, UserDetailView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('', UserListCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
]
