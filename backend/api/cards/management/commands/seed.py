""" Cards Commands module """
# Django
from django.core.management.base import BaseCommand

# Models
from api.cards.models import WhiteCard, BlackCard

class Command(BaseCommand):
    """ Cards command """
    help = "Seed database for testing and development"

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding cards data...')
        self.run_seed(options['mode'])
        self.stdout.write('done.')

    def create_white_card(self, number):
      wcard = WhiteCard(
        text="Carta blanca #{}".format(number)
      )
      wcard.save()
     
      
    def create_black_card(self, number):
      wcard = BlackCard(
        text="Carta negra #{}".format(number)
      )
      wcard.save()
     


    def run_seed(self, mode):
      for i in range(15):
        self.create_white_card(i)
      
      for i in range(15):
        self.create_black_card(i)

  
