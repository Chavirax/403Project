from django.urls import path
from .views import displayLotsPageView
from .views import showULotsPageView
from .views import showYLotsPageView
from .views import showALotsPageView
from .views import showBLotsPageView
from .views import showCLotsPageView
from .views import showLotsPageView
from .views import searchEmpPageView
from .views import findEmpPageView
from .views import empPageView
from .views import storeEmpPageView
from .views import updateEmpPageView
from .views import deleteEmpPageView
from .views import addEmpPageView

  

urlpatterns = [
    path("Ulots/", showULotsPageView, name="Ulots"),
    path("YLots/", showYLotsPageView, name="YLots"),
    path("ALots/", showALotsPageView, name="ALots"),
    path("BLots/", showBLotsPageView, name="BLots"),
    path("CLots/", showCLotsPageView, name="CLots"),
    path('showLots/', showLotsPageView, name= 'showLots'),
    path("searchemp/", searchEmpPageView, name="searchemp"),
    path("findemp/", findEmpPageView, name="findemp"),  
    path("emp/", empPageView, name="employee"), 
    path("addemp/", addEmpPageView, name="addemp"),            
    path("storeemp/", storeEmpPageView, name="storeemp"),
    path("update/", updateEmpPageView, name="update"),
    path("delete/", deleteEmpPageView, name="delete"),



]