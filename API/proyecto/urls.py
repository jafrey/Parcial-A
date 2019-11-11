from django.conf.urls import  include, url

from django.contrib import admin

from rest_framework import routers

#importa views, donde se encuentran los viewsets

from aplicacion import views

router = routers.DefaultRouter()
router.register(r'-users', views.UserViewSet)
router.register(r'-groups', views.GroupViewSet)
router.register(r'-canciones', views.CancionViewSet)
router.register(r'-usuario', views.UsuarioViewSet)



admin.autodiscover()

urlpatterns = [
    url(r'^api-root', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', views.login),
]
