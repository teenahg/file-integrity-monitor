from django.urls import path, re_path
from app import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    # The Files Dashboard Page
    path('files/', views.files, name='files'),
    path('output/', views.output),
    path('output/', views.output, name='script'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]