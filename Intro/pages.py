from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class BasicIntro(Page):
    timeout_seconds = 120
    form_model = 'player'
    form_fields = ['prolificid']

    def before_next_page(self):
        self.group.determine_nicknames()


class GameInstructions(Page):
    timeout_seconds = 600

    def vars_for_template(self):
        return {"name": self.player.participant.vars['nickname']}


class TestingUnderstanding1(Page):
    form_model = 'player'
    form_fields = ['und1']
    timeout_seconds = 20


class TestingUnderstanding1R(Page):
    timeout_seconds = 20


class TestingUnderstanding2(Page):
    form_model = 'player'
    form_fields = ['und2']
    timeout_seconds = 20


class TestingUnderstanding2R(Page):
    timeout_seconds = 20


class TestingUnderstanding3(Page):
    form_model = 'player'
    form_fields = ['und3']
    timeout_seconds = 20


class TestingUnderstanding3R(Page):
    timeout_seconds = 20


class TestingUnderstanding4(Page):
    form_model = 'player'
    form_fields = ['und4']
    timeout_seconds = 20


class TestingUnderstanding4R(Page):
    timeout_seconds = 20


class TestingUnderstanding5(Page):
    form_model = 'player'
    form_fields = ['und5']
    timeout_seconds = 20


class TestingUnderstanding5R(Page):
    timeout_seconds = 20


class UnderstandGame(Page):
    form_model = 'player'
    form_fields = ['under']
    timeout_seconds = 30

    def before_next_page(self):
        self.group.count_waiting()


class SecondInstructions(Page):
    def is_displayed(self):
        return self.player.under == 0
    timeout_seconds = 180

    def vars_for_template(self):
        return {"name": self.player.participant.vars['nickname']}


class WaitingPage(WaitPage):
    template_name = 'Intro/WaitingPage.html'

    def vars_for_template(self):
        return {"num": sum([p.player_count for p in self.group.get_players()])}


class PreGame(Page):
    timeout_seconds = 30


page_sequence = [
    BasicIntro,
    GameInstructions,
    TestingUnderstanding1,
    TestingUnderstanding1R,
    TestingUnderstanding2,
    TestingUnderstanding2R,
    TestingUnderstanding3,
    TestingUnderstanding3R,
    TestingUnderstanding4,
    TestingUnderstanding4R,
    TestingUnderstanding5,
    TestingUnderstanding5R,
    UnderstandGame,
    SecondInstructions,
    WaitingPage,
    PreGame
]
