from django.conf.urls import url, include
from rest_framework import routers
from framework.views import CategoryViewSet


router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]