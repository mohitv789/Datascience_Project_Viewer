
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.machinelearning , name = 'machine_learning'),
    path('about', views.about , name = 'about'),
    path('guide', views.guide , name = 'guide'),
    path('contact', views.contact , name = 'contact'),
    path('create', views.create , name = 'create'),
    path('<int:machine_learning_id>', views.detail , name = 'detail'),
]
