from django.urls import path, re_path
from app import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('results', views.button),
    path('output_results', views.res, name='output_results'),
    path('all', views.all, name='all'),
    path('external', views.external),
    path('continues', views.continues),
    path('compare', views.compare, name='compare'),
    # The Files Dashboard Page
    path('files/', views.files, name='files'),
    path('output/', views.output),
    path('output/', views.output, name='script'),
    path('users/', views.users, name='users'),
    path('verify/', views.verify, name='verify'),
    path('checksum_verification/', views.checksum_verification, name='checksum_verification'),
    path('verification_results/', views.verification_results, name='verification_results'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    
]