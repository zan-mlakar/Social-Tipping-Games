from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Žan Mlakar'

doc = """
Social Tipping Game - Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'thesis_intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_player_names(self):
        print('setting player names')
        for player in self.get_players():
            player.participant.vars['player_name'] = player.own_name


class Player(BasePlayer):
    own_name = models.StringField()

    und1 = models.BooleanField()
    und2 = models.BooleanField()
    und3 = models.BooleanField()
    und4 = models.BooleanField()
    und5 = models.BooleanField()
    cund1 = models.BooleanField()
    cund2 = models.BooleanField()
    cund3 = models.BooleanField()
    cund4 = models.BooleanField()
    cund5 = models.BooleanField()

    under = models.BooleanField()
