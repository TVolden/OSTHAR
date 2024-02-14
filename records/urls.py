from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:session>', views.records, name="records"),
    path('<uuid:session>/<int:subject_id>/', views.observation, name="observation"),
    path('<uuid:session>/results/', views.results, name="results"),
    path('<uuid:session>/export/', views.export, name="export"),
    # Ajax apis
    path('<uuid:session>/observations/<int:record_id>/', views.record, name="record"),
]