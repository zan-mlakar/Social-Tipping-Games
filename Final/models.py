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
    pass


class Player(BasePlayer):
    # Demographics and suspicion questions #
    age = models.IntegerField(
        label='What is your current age (in years)?',
        min=13, max=100)
    gender = models.StringField(
        choices=['Male', 'Female', 'Other', 'Prefer not to declare'],
        label='What is your gender?',
        widget=widgets.RadioSelectHorizontal)
    education = models.StringField(
        choices=['Some high school', 'High school diploma', 'Some college', 'Completed vocational training',
                 'Bachelor degree', 'Master degree', 'PhD diploma'],
        label='What is the highest level of education you have completed?',
        widget=widgets.RadioSelectHorizontal)
    comments = models.LongStringField(
        label='Do you have any final thoughts on the study or anything you would like to share with the experimenters?',
        blank=True)
    prolificid = models.StringField(
        label='Enter your Prolific ID:',
        blank=False)
