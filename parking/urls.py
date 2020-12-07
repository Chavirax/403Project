from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import contactPageView
from .views import registerPageView
from .views import loginPageView


urlpatterns = [
    path("about/<str:lot_name>/<int:parking_cost>",aboutPageView, name="about1"),
    path("about/",aboutPageView, name="about"),
    path("contact/<str:contact_name>/<str:contact_email>",contactPageView, name="contact"),
    path("vehicleRegistration/",registerPageView, name='registration'),
    path("login/", loginPageView, name='login'),
    path("",indexPageView, name='index'),


]
