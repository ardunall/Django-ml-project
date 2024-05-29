from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="home"),
    path("ml", views.ml, name="ml"),
    path('department/<int:department_id>/', views.department_detail, name='department_detail'),

]
