from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('predictor/', views.predictor, name="predictor"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard_pdf/', views.dashboard_pdf, name="dashboard_pdf")

]