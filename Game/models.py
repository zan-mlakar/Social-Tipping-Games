import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Žan Mlakar'

doc = """
The product launch game.
"""


class Constants(BaseConstants):
    name_in_url = 'game'
    players_per_group = None
    num_rounds = 24


class Subsession(BaseSubsession):
    def creating_session(self):
        print('Creating session', self.round_number)
        self.session.vars['max_rounds'] = 24
        self.session.vars['break_round'] = 24


class Group(BaseGroup):
    def total_players(self):
        for p in self.get_players():
            p.total_players = len(self.get_players())

    def number_confederates(self):
        for p in self.get_players():
            if p.total_players == 9:
                p.num_conf = 3
            else:
                p.num_conf = 4

    def determine_nicknames(self):
        for p in self.get_players():
            if 'nickname' not in p.participant.vars:
                print('Determining and storing player nicknames')
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

    def payoff_decrease(self):
        print('Calculating payoff ...')
        for p in self.get_players():
            p.payoff_left = (240 - (self.subsession.round_number*5))

    def chosen_option(self):
        print('Calculating chosen options ...')
        for p in self.get_players():
            if p.chosen_name == 'Tao':
                p.chose_tao = 1
            elif p.chosen_name == 'Eta':
                p.chose_eta = 1
        sum_eta = sum([p.chose_eta for p in self.get_players()])
        sum_tao = sum([p.chose_tao for p in self.get_players()])
        for p in self.get_players():
            if p.chosen_name == '' and sum_eta > sum_tao:
                p.chose_eta = 1
            elif p.chosen_name == '' and (sum_tao > sum_eta or sum_tao == sum_eta):
                p.chose_tao = 1

    def confederate_strategy(self):
        sum_eta = sum([p.chose_eta for p in self.get_players()])
        sum_tao = sum([p.chose_tao for p in self.get_players()])
        self.get_player_by_id(1).con_conf = random.randint(0, 2)
        self.get_player_by_id(1).ran_conf = random.randint(0, 1)
        print('Break-round ...')
        if sum_eta <= 1 or sum_tao <= 1:
            print('     !!!Current round is the break round!!!')
            self.get_player_by_id(1).con_strategy = 1
        for p in self.get_player_by_id(1).in_previous_rounds():
            if p.con_strategy == 1:
                print('     !!!Current round is a post-break round!!!')
                self.get_player_by_id(1).con_strategy = 2

    def break_name(self):
        sum_eta = sum([p.chose_eta for p in self.get_players()])
        sum_tao = sum([p.chose_tao for p in self.get_players()])
        if self.get_player_by_id(1).con_strategy == 1:
            if sum_tao <= 1:
                print('     Break name is Tao')
                self.get_player_by_id(1).break_name = 1
            elif sum_eta <= 1:
                print('     Break name is Eta')
                self.get_player_by_id(1).break_name = 2
        for p in self.get_player_by_id(1).in_previous_rounds():
            if p.break_name == 1:
                print('     Break name is Tao')
                self.get_player_by_id(1).break_name = 1
            elif p.break_name == 2:
                print('     Break name is Eta')
                self.get_player_by_id(1).break_name = 2

    def confederate_activity(self):
        con_strategy = self.get_player_by_id(1).con_strategy
        sum_eta = sum([p.chose_eta for p in self.get_players()])
        sum_tao = sum([p.chose_tao for p in self.get_players()])
        break_name = self.get_player_by_id(1).break_name
        num_conf = self.get_player_by_id(1).num_conf
        con_conf = self.get_player_by_id(1).con_conf
        print('Strategy ...')
        if con_strategy == 0:
            print('     Stage 1:')
            if sum_eta == sum_tao or sum_tao > sum_eta:
                print('     A) Assigning more to Tao')
                if num_conf == 3:
                    self.get_player_by_id(1).conf_tao = 2
                    self.get_player_by_id(1).conf_eta = 1
                elif num_conf == 4:
                    self.get_player_by_id(1).conf_tao = 3
                    self.get_player_by_id(1).conf_eta = 1
            elif sum_tao < sum_eta:
                print('     B) Assigning more to Eta')
                if num_conf == 3:
                    self.get_player_by_id(1).conf_tao = 1
                    self.get_player_by_id(1).conf_eta = 2
                elif num_conf == 4:
                    self.get_player_by_id(1).conf_tao = 1
                    self.get_player_by_id(1).conf_eta = 3
        else:
            print('     Stage 2:')
            if break_name == 1:
                print('     A) Consistent Tao now')
                if num_conf == 3:
                    self.get_player_by_id(1).conf_tao = num_conf
                    self.get_player_by_id(1).conf_eta = 0
                elif num_conf == 4:
                    self.get_player_by_id(1).conf_tao = num_conf - con_conf
                    self.get_player_by_id(1).conf_eta = con_conf
                if sum_eta == 0:
                    self.get_player_by_id(1).conf_tao = num_conf
                    self.get_player_by_id(1).conf_eta = 0
            elif break_name == 2:
                print('     B) Consistent Eta now')
                if num_conf == 3:
                    self.get_player_by_id(1).conf_tao = 0
                    self.get_player_by_id(1).conf_eta = num_conf
                elif num_conf == 4:
                    self.get_player_by_id(1).conf_tao = con_conf
                    self.get_player_by_id(1).conf_eta = num_conf - con_conf
                if sum_tao == 0:
                    self.get_player_by_id(1).conf_tao = 0
                    self.get_player_by_id(1).conf_eta = num_conf

    def same_choice(self):
        print('Comparing choices ...')
        total_players = self.get_player_by_id(1).total_players
        total_choices = sum([p.chose_tao for p in self.get_players()])
        if total_choices == 0 and self.get_player_by_id(1).break_name == 2:
            print('     !!!Everyone chose Eta!!!')
            self.session.vars['max_rounds'] = self.subsession.round_number
        elif total_choices == total_players and self.get_player_by_id(1).break_name == 1:
            print('     !!!Everyone chose Tao!!!')
            self.session.vars['max_rounds'] = self.subsession.round_number
        else:
            print('     Choices are different')

    def assign_names(self):
        print('Calculating chosen names ...')
        for p in self.get_players():
            if p.chose_tao == 1:
                p.tao_names = p.participant.vars['nickname']
            else:
                p.eta_names = p.participant.vars['nickname']
        con_strategy = self.get_player_by_id(1).con_strategy
        break_name = self.get_player_by_id(1).break_name
        ran_conf = self.get_player_by_id(1).ran_conf
        con_conf = self.get_player_by_id(1).con_conf
        num_conf = self.get_player_by_id(1).num_conf
        sum_eta = sum([p.chose_eta for p in self.get_players()])
        sum_tao = sum([p.chose_tao for p in self.get_players()])
        self.session.vars['conf_tao_names'] = ['']
        self.session.vars['conf_eta_names'] = ['']
        if con_strategy == 0:
            if sum_eta == sum_tao or sum_tao > sum_eta:
                print('     A) Assigning more names to Tao')
                if num_conf == 3:
                    self.session.vars['conf_tao_names'] = ['Player 2', 'Player 6']
                    self.session.vars['conf_eta_names'] = ['Player 10']
                elif num_conf == 4:
                    self.session.vars['conf_tao_names'] = ['Player 2', 'Player 9', 'Player 10']
                    self.session.vars['conf_eta_names'] = ['Player 6']
            elif sum_tao < sum_eta:
                print('     B) Assigning more names to Eta')
                if num_conf == 3:
                    self.session.vars['conf_eta_names'] = ['Player 2', 'Player 6']
                    self.session.vars['conf_tao_names'] = ['Player 10']
                elif num_conf == 4:
                    self.session.vars['conf_eta_names'] = ['Player 2', 'Player 9', 'Player 10']
                    self.session.vars['conf_tao_names'] = ['Player 6']
        elif break_name == 1:
            if num_conf == 3:
                self.session.vars['conf_tao_names'] = ['Player 2', 'Player 6', 'Player 10']
                self.session.vars['conf_eta_names'] = ['']
            if num_conf == 4:
                if con_conf == 0:
                    self.session.vars['conf_tao_names'] = ['Player 2', 'Player 6', 'Player 9', 'Player 10']
                    self.session.vars['conf_eta_names'] = ['']
                if con_conf == 1:
                    if ran_conf == 0:
                        self.session.vars['conf_tao_names'] = ['Player 2', 'Player 9', 'Player 10']
                        self.session.vars['conf_eta_names'] = ['Player 6']
                    elif ran_conf == 1:
                        self.session.vars['conf_tao_names'] = ['Player 2', 'Player 6', 'Player 10']
                        self.session.vars['conf_eta_names'] = ['Player 9']
                if con_conf == 2:
                    self.session.vars['conf_tao_names'] = ['Player 2', 'Player 10']
                    self.session.vars['conf_eta_names'] = ['Player 6', 'Player 9']
            if sum_eta == 0:
                self.session.vars['conf_tao_names'] = ['Player 2', 'Player 6', 'Player 9', 'Player 10']
                self.session.vars['conf_eta_names'] = ['']
        elif break_name == 2:
            if num_conf == 3:
                self.session.vars['conf_eta_names'] = ['Player 2', 'Player 6', 'Player 10']
                self.session.vars['conf_tao_names'] = ['']
            if num_conf == 4:
                if con_conf == 0:
                    self.session.vars['conf_eta_names'] = ['Player 2', 'Player 6', 'Player 9', 'Player 10']
                    self.session.vars['conf_tao_names'] = ['']
                if con_conf == 1:
                    if ran_conf == 0:
                        self.session.vars['conf_eta_names'] = ['Player 2', 'Player 9', 'Player 10']
                        self.session.vars['conf_tao_names'] = ['Player 6']
                    elif ran_conf == 1:
                        self.session.vars['conf_eta_names'] = ['Player 2', 'Player 6', 'Player 10']
                        self.session.vars['conf_tao_names'] = ['Player 9']
                if con_conf == 2:
                    self.session.vars['conf_eta_names'] = ['Player 2', 'Player 10']
                    self.session.vars['conf_tao_names'] = ['Player 6', 'Player 9']
            if sum_tao == 0:
                self.session.vars['conf_eta_names'] = ['Player 2', 'Player 6', 'Player 9', 'Player 10']
                self.session.vars['conf_tao_names'] = ['']
        self.session.vars['total_tao_names'] = [p.tao_names for p in self.get_players() if p.tao_names is not None] + self.session.vars['conf_tao_names']
        self.session.vars['total_tao_names'] = random.sample(self.session.vars['total_tao_names'], len(self.session.vars['total_tao_names']))
        self.session.vars['total_eta_names'] = [p.eta_names for p in self.get_players() if p.eta_names is not None] + self.session.vars['conf_eta_names']
        self.session.vars['total_eta_names'] = random.sample(self.session.vars['total_eta_names'], len(self.session.vars['total_eta_names']))


class Player(BasePlayer):
    chosen_name = models.StringField(
        choices=['Tao', 'Eta']
    )

    total_players = models.IntegerField()
    nickname_number = models.IntegerField()
    chose_eta = models.IntegerField(initial=0)
    chose_tao = models.IntegerField(initial=0)
    payoff_left = models.IntegerField(initial=240)
    con_strategy = models.IntegerField(initial=0)
    break_name = models.IntegerField(initial=0)
    num_conf = models.IntegerField()
    con_conf = models.IntegerField()
    ran_conf = models.IntegerField()
    conf_tao = models.IntegerField()
    conf_eta = models.IntegerField()
    tao_names = models.StringField(initial='     ')
    eta_names = models.StringField(initial='     ')
