from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

# crear ruta, viewset y nombre
router.register("api/projects", ProjectViewSet, "projects")

urlpatterns = router.urls 