""" Cards models """

# Django
from django.db import models


class Card(models.Model):
    """ Card model. 
        A card is a playable object for creating funny phrases 
        that sums points to the player.
    """
    text = models.CharField("Card  description", max_length=200)

    def __str__(self):
        """ Return card text """
        return self.text

    class Meta:
        abstract = True

class WhiteCard(Card):
    """ WhiteCard Model 
        A white card allows player to make a funny phrase. 
    """


class BlackCard(Card):
    """ BlackCard model 
        A black card is a card played by the Zar to allow players
        to completed the phrase in the card. 
    """

    phrase_space = models.PositiveIntegerField(
        "Number of phrases",
        default=1,
        help_text="Number of phrases needed to complete the card sentence"
    )
