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
    def determine_nicknames(self):
        print('Determining and storing player nicknames')
        for p in self.get_players():
            if p.id_in_group == 1 or p.id_in_group == 9:
                p.nickname_number = p.id_in_group
            elif 1 < p.id_in_group < 5:
                p.nickname_number = p.id_in_group + 1
            elif 4 < p.id_in_group < 7:
                p.nickname_number = p.id_in_group + 2
            elif 6 < p.id_in_group < 9:
                p.nickname_number = p.id_in_group + 4
            names = ('Player', str(p.nickname_number))
            p.participant.vars['nickname'] = ' '.join(names)

    def count_waiting(self):
        for p in self.get_players():
            if p.under == 2:
                p.player_count = 1
            else:
                p.player_count = 0


class Player(BasePlayer):
    und1 = models.BooleanField(initial=False)
    und2 = models.BooleanField(initial=False)
    und3 = models.BooleanField(initial=False)
    und4 = models.BooleanField(initial=False)
    und5 = models.BooleanField(initial=False)
    under = models.IntegerField(initial=2)

    nickname_number = models.IntegerField()
    player_count = models.IntegerField(initial=1)

    prolificid = models.StringField(
        label='Enter your Prolific ID:',
        blank=False)
