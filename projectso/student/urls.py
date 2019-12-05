from rest_framework import routers

from .viewsets import StudentViewSet

router = routers.SimpleRouter()
router.register('students', StudentViewSet)

urlpatterns = router.urls
