from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from random import shuffle


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'prolificid', 'comments']


class FinalPage(Page):
    pass


page_sequence = [
    Demographics,
    FinalPage
]
