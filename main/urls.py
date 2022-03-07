from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("contacts/", views.about_page, name="contactspage")
]