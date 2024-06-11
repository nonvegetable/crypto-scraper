from django.urls import path
from . import views

urlpatterns = [
    path('api/taskmanager/start_scraping/', views.StartScrapingView.as_view(), name='start_scraping'),
    path('api/taskmanager/scraping_status/<str:job_id>/', views.ScrapingStatusView.as_view(), name='scraping_status'),
]
