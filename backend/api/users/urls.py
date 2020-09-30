""" Users URL's """

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter
# Views
from api.users import views as users_views

router = DefaultRouter()
router.register(r'users', users_views.UserViewSet)
router.register(r'users', users_views.UserCreateViewSet)

urlpatterns = [
  path('', include(router.urls))
]