""" Cards urls """

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import WhiteCardViewSet, BlackCardViewSet
 

router = DefaultRouter()
router.register(r'white-cards', WhiteCardViewSet)
router.register(r'black-cards', BlackCardViewSet)

urlpatterns = [
    path('', include(router.urls))
]
