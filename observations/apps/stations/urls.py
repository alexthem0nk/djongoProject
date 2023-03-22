from rest_framework import routers

from .views import stationsViewSet

router = routers.SimpleRouter()
router.register("", stationsViewSet)
urlpatterns = router.urls
