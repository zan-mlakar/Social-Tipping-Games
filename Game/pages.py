from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Choice(Page):
    def is_displayed(self):
        return self.subsession.round_number <= self.session.vars['max_rounds']

    def vars_for_template(self):
        if self.round_number == 1:
            return {'group_payoff': self.player.payoff_left}
        else:
            return {'group_payoff': self.player.in_round(self.round_number - 1).payoff_left}

    timeout_seconds = 15
    form_model = 'player'
    form_fields = ['chosen_name']


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.subsession.round_number <= self.session.vars['max_rounds']

    def after_all_players_arrive(self):
        self.group.total_players()
        self.group.number_confederates()
        self.group.determine_nicknames()
        self.group.payoff_decrease()
        self.group.chosen_option()
        self.group.confederate_strategy()
        self.group.break_name()
        self.group.confederate_activity()
        self.group.same_choice()
        self.group.assign_names()


class Results(Page):
    def is_displayed(self):
        return self.subsession.round_number <= self.session.vars['max_rounds']

    def vars_for_template(self):
        return {
            'chose_tao':
                round(((sum([p.chose_tao for p in self.group.get_players()]) + self.group.get_player_by_id(1).conf_tao) / (self.player.total_players + self.player.num_conf)) * 100, 2),
            'chose_eta':
                round(((sum([p.chose_eta for p in self.group.get_players()]) + self.group.get_player_by_id(1).conf_eta) / (self.player.total_players + self.player.num_conf)) * 100, 2),
            'names_tao':
                (self.session.vars['total_tao_names']),
            'names_eta':
                (self.session.vars['total_eta_names'])
        }

    timeout_seconds = 15


page_sequence = [
    Choice,
    ResultsWaitPage,
    Results
]
