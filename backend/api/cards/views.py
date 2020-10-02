# Django REST Framework
from rest_framework import viewsets

# Serializers
from .serializers import WhiteCardModelSerializer, BlackCardModelSerializer
# Models
from .models import WhiteCard, BlackCard

class WhiteCardViewSet(viewsets.ModelViewSet):
    """WhiteCard view set  """

    queryset = WhiteCard.objects.all()
    serializer_class = WhiteCardModelSerializer

class BlackCardViewSet(viewsets.ModelViewSet):
    """BlackCard view set  """

    queryset = BlackCard.objects.all()
    serializer_class = BlackCardModelSerializer
