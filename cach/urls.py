from django.urls import path

from .views import *


urlpatterns = [
    path("company/", CompanyListView.as_view()),
]
