from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Žan Mlakar'

doc = """
Introduction to the Product launch game.
"""


class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    und1 = models.BooleanField(initial=False)
    und2 = models.BooleanField(initial=False)
    und3 = models.BooleanField(initial=False)
    und4 = models.BooleanField(initial=False)
    und5 = models.BooleanField(initial=False)
    under = models.BooleanField(initial=False)
