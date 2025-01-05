from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from game.views import GameViewSet, CardViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('authentication.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 