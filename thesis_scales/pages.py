from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from random import shuffle


class SecondIntro(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13


class SecondIntroC(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13


class GameQuestions(Page):
    form_model = 'player'
    form_fields = ['man1', 'man2', 'exd1', 'exd2', 'exd3r', 'exd4', 'exd5r', 'exd6r', 'exd7r', 'exd8r']


class NFA(Page):
    form_model = 'player'
    form_fields = ['nfa1', 'nfa2', 'nfa3', 'nfa4', 'nfa5', 'nfc']


class BISBAS1(Page):
    form_model = 'player'
    form_fields = ['bis1', 'bis3', 'bis5', 'basr1', 'basr3', 'basr5', 'basd1', 'basd3', 'basf1', 'basf3']


class BISBAS2(Page):
    form_model = 'player'
    form_fields = ['bis2', 'bis4', 'bis6', 'bis7', 'basr2', 'basr4', 'basd2', 'basd4', 'basf2', 'basf4']


class IMP(Page):
    form_model = 'player'
    form_fields = ['impa1r', 'impn1r', 'impm1', 'impa2r', 'impn2r', 'impm2', 'impa3r', 'impm3', 'impa4', 'impm4', 'impn3r', 'impa5r', 'impn4r']


class SCC(Page):
    form_model = 'player'
    form_fields = ['scc1r', 'scc2r', 'scc3r', 'scc4r', 'scc5r', 'scc6', 'scc7r', 'scc8r', 'scc9r', 'scc10r', 'scc11', 'scc12r']


class SDS(Page):
    form_model = 'player'
    form_fields = ['sds1', 'sds2', 'sds3', 'sds4', 'sds5', 'sds6', 'sds7', 'sds8', 'sds9', 'sds10', 'sds11', 'sds12', 'sds13']


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'religion', 'sus1', 'sus2', 'feed1', 'feed2', 'feed3', 'comments']


class FinalPage(Page):
    pass


page_sequence = [
    SecondIntro,
    SecondIntroC,
    GameQuestions,
    NFA,
    BISBAS1,
    BISBAS2,
    IMP,
    SCC,
    SDS,
    Demographics,
    FinalPage
]
