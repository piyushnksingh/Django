from django.urls import path
from . import views

urlpatterns = [
    # path("",views.review), # when view is function
    path("",views.ReviewView.as_view()), # when view is class
    path("thank-you",views.thank_you),
]