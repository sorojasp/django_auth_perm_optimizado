from homes import views
from django.urls import include, path

urlpatterns = [
        path('main/', views.HomeView.as_view()),
]
