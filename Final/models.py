from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Žan Mlakar'

doc = """
Demographic questions and debriefing.
"""


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def total_players(self):
        for p in self.get_players():
            p.total_players = len(self.get_players())


class Player(BasePlayer):
    confcon = models.IntegerField(
        label='I think Players 2, 6, and 10 were confident in the New Product they were choosing '
              'during the game.',
        choices=((1, 'Strongly disagree'), (2, 'Disagree'),
                 (3, 'Neither agree nor disagree'), (4, 'Agree'), (5, 'Strongly agree')),
        widget=widgets.RadioSelectHorizontal)
    confincon = models.IntegerField(
        label='I think Players 2, 6, 9, and 10 were confident in the New Product they were choosing '
              'during the game.',
        choices=((1, 'Strongly disagree'), (2, 'Disagree'),
                 (3, 'Neither agree nor disagree'), (4, 'Agree'), (5, 'Strongly agree')),
        widget=widgets.RadioSelectHorizontal)
    intracon = models.IntegerField(
        label='I think Players 2, 6, and 10 were unlikely to change their New Product choice and side with '
              'the rest of the group.',
        choices=((1, 'Strongly disagree'), (2, 'Disagree'),
                 (3, 'Neither agree nor disagree'), (4, 'Agree'), (5, 'Strongly agree')),
        widget=widgets.RadioSelectHorizontal)
    intraincon = models.IntegerField(
        label='I think Players 2, 6, 9, and 10 were unlikely to change their New Product choice and side with '
              'the rest of the group.',
        choices=((1, 'Strongly disagree'), (2, 'Disagree'),
                 (3, 'Neither agree nor disagree'), (4, 'Agree'), (5, 'Strongly agree')),
        widget=widgets.RadioSelectHorizontal)

    total_players = models.IntegerField()

    # Demographics and suspicion questions #
    age = models.IntegerField(
        label='What is your current age (in years)?',
        min=13, max=100)
    gender = models.StringField(
        choices=['Male', 'Female', 'Other', 'Prefer not to declare'],
        label='What is your gender?',
        widget=widgets.RadioSelectHorizontal)
    comments = models.LongStringField(
        label='Do you have any final thoughts on the study or anything you would like to share with the researchers?',
        blank=True)
