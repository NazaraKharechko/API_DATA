from django.urls import path
from . import views
from .views import cramp, CreateVieAll, FindVieData

urlpatterns = [
    path('', views.cramp),
    path('all/', CreateVieAll.as_view()),
    path('find/', FindVieData.as_view())
]
