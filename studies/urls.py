from django.urls import path
from . import views

urlpatterns = [
    path('', views.studies, name="studies"),
    path('<str:study>/', views.study, name="study"),
    path('<str:study>/<str:institution>/<str:trial>/', views.standby, name="standby"),
    path('<str:study>/<str:institution>/<str:trial>/subjects', views.subjects, name="subjects"),
]