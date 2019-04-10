from django.conf.urls import url, include
from rest_framework import routers
from framework.views import CategoryViewSet, ReceiptViewSet

app_name = 'framework'

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'receipt', ReceiptViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # TODO - api-auth appears broken, but are we authenticating through REST?
]