""" Cards serializers """

# Django Rest Framework
from rest_framework import serializers

# Models
from .models import WhiteCard, BlackCard

class WhiteCardModelSerializer(serializers.ModelSerializer):
    """WhiteCard Model Serializer  """

    class Meta: 
      """ Meta class """
      model = WhiteCard
      fields = (
        'text', 
      )


class BlackCardModelSerializer(serializers.ModelSerializer):
    """ BlackCard Model Serializer """

    class Meta: 
      """ Meta class """
      model = BlackCard
      fields = (
        'text',
        'phrase_space'
        )