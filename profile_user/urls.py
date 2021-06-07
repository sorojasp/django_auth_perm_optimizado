from profile_user import views
from django.urls import include, path

urlpatterns = [
    path('main/', views.UserView.as_view()),
]
