from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from friendmap import views

router = routers.DefaultRouter()
router.register(r'friendmaps', views.FriendmapView, 'friendmap')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]