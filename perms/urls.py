from perms import views
from django.urls import include, path

urlpatterns = [
    path('main/', views.PermsView.as_view()),
]
