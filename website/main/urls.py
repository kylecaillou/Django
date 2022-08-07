from django.urls import path

from . import views

urlpatterns = [

    path("<int:id>", views.index, name="index"),
    path("page1/", views.page1, name="page1"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
]
