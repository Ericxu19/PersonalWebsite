from django.urls import path
from . import views

app_name = 'Main'
urlpatterns = [
    path('about/', views.about, name="about"),
    path('projects/', views.project_index, name="project_index"),
    path('work/', views.work, name="work"),
    path('resume/', views.resume, name="resume"),
]