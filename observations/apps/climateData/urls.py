"""from rest_framework import routers
from django.urls import path
from .views import climateDataViewSet

router = routers.SimpleRouter()
router.register("", climateDataViewSet)
urlpatterns = router.urls"""

from django.urls import path, include
from rest_framework import routers
from .views import climateDataViewSet

# from .views import CustomLoginView


router = routers.DefaultRouter()
router.register("", climateDataViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
