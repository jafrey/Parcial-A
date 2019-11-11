from django.conf.urls import  include, url

from django.contrib import admin

from rest_framework import routers
from aplicacion import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'canciones', views.CancionViewSet)


admin.autodiscover()

urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
