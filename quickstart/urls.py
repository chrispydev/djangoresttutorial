from django.urls import include, path
from rest_framework import routers
from quickstart import views

routers = routers.DefaultRouter()
routers.register(r'users', views.UserViewSet)
routers.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]