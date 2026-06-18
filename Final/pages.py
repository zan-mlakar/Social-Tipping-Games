from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from random import shuffle


class Start(Page):
    def before_next_page(self):
        self.group.total_players()


class PreFinalCon(Page):
    def is_displayed(self):
        return self.player.total_players == 9
    form_model = 'player'
    form_fields = ['confcon', 'intracon', 'age', 'gender', 'comments']


class PreFinalIncon(Page):
    def is_displayed(self):
        return self.player.total_players < 9
    form_model = 'player'
    form_fields = ['confincon', 'intraincon', 'age', 'gender', 'comments']


class FinalPage(Page):
    pass


page_sequence = [
    Start,
    PreFinalCon,
    PreFinalIncon,
    FinalPage
]
