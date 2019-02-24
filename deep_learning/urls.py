
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.deeplearning , name = 'deep_learning'),
    path('create', views.dl_create , name = 'create2'),
    path('<int:deep_learning_id>', views.detail2 , name = 'detail2'),
]
