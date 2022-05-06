from django.urls import path
from .views import home_view, contact_view, Detail_view

urlpatterns = [
    path('', home_view, name="home"),
    path('contact', contact_view, name="contact"),
    path('postdetail/<str:slug>/', Detail_view, name="postdetail"),
]
