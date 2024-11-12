from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Žan Mlakar'

doc = """
Social Tipping Game - Self-Reported Measures of Individual Characteristics
"""


class Constants(BaseConstants):
    name_in_url = 'thesisquestiondemo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Manipulation checks and game-related questions #
    def gmq(x):
        return models.IntegerField(
            choices=[[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Neither agree nor disagree'], [4, 'Agree'],
                     [5, 'Strongly agree']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    man1 = gmq('Other participants could see the New Product endorsements I made in the game.')
    man2 = gmq('During the task, I felt exposed.')
    exd1 = gmq('I felt free to do whatever I want.')
    exd2 = gmq('My New Product endorsements were impulsive.')
    exd3r = gmq('I felt like I was being judged by the other participants.')
    exd4 = gmq('I endorsed a New Product in each round quickly.')
    exd5r = gmq('When making my New Product endorsements, I felt limited by what other employees endorsed.')
    exd6r = gmq('I worried about making the wrong endorsement.')
    exd7r = gmq('I felt a pressure to conform to the majority.')
    exd8r = gmq('I thought a lot about the optimal New Product endorsement in each round.')


    # Need for affiliation scale #
    def nfa(x):
        return models.IntegerField(
            choices=[[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Somewhat disagree'],
                     [4, 'Neither agree nor disagree'], [5, 'Somewhat agree'], [6, 'Agree'],
                     [7, 'Strongly agree']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    nfa1 = nfa('I think being close to others, listening to them, and relating to them is one of my favourite and most satisfying pasttimes.')
    nfa2 = nfa('I would find it very satisfying to be able to form new friendships with whomever I liked.')
    nfa3 = nfa('I think I get satisfaction out of contact with others more than most people realise.')
    nfa4 = nfa('The main thing I like about being around other people is the warm glow I get from contact with them.')
    nfa5 = nfa('I think it would be satisfying if I could have very close friendships with quite a few people.')

    # BIS and BAS scales #
    def bis_bas(x):
        return models.IntegerField(
            choices=[[1, 'Completely disagree'], [2, 'Partially disagree'],
                     [3, 'Partially agree'], [4, 'Completely agree']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    bis1 = bis_bas('If I think something unpleasant is going to happen, I usually get pretty "worked up".')
    bis2 = bis_bas('I worry about making mistakes.')
    bis3 = bis_bas('Criticism or scolding hurts me quite a bit.')
    bis4 = bis_bas('I feel pretty worried or upset when I think or know somebody is angry at me.')
    bis5 = bis_bas('Even if something bad is about to happen to me, I rarely experience fear or nervousness.')
    bis6 = bis_bas('I feel worried when I think I have done poorly at something.')
    bis7 = bis_bas('I have very few fears compared to my friends.')
    basr1 = bis_bas('When I get something I want, I feel excited and energised.')
    basr2 = bis_bas('When I am doing well at something, I love to keep at it.')
    basr3 = bis_bas('When good things happen to me, it affects me strongly.')
    basr4 = bis_bas('It would excite me to win a contest.')
    basr5 = bis_bas('When I see an opportunity for something I like, I get excited right away.')
    basd1 = bis_bas('When I want something, I usually go all-out to get it.')
    basd2 = bis_bas('I go out of my way to get things I want.')
    basd3 = bis_bas('If I see a chance to get something I want, I move on it right away.')
    basd4 = bis_bas('When I go after something I use a "no holds barred" approach.')
    basf1 = bis_bas('I will often do things for no other reason than that they might be fun.')
    basf2 = bis_bas('I crave excitement and new sensations.')
    basf3 = bis_bas('I am always willing to try something new if I think it will be fun.')
    basf4 = bis_bas('I often act on the spur of the moment.')

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
    religion = models.StringField(
        choices=['Christianity', 'Judaism', 'Islam', 'Hinduism', 'Buddhism', 'Atheism', 'Agnosticism', 'Other',
                 'Prefer not to declare'],
        label='Which religion do you most closely associate with?',
        widget=widgets.RadioSelectHorizontal)
    sus1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='Do you personally know any of the participants that entered the lab at the same time as you?',
        widget=widgets.RadioSelectHorizontal)
    sus2 = models.StringField(label='What do you think the study was about?', blank=True)
    feed1 = models.StringField(label='Was the presentation of information before and during the game clear?',
                               blank=True)
    feed2 = models.StringField(label='Did you find any part of the game instructions to be (too) complex?',
                               blank=True)
    feed3 = models.StringField(label='Was your behaviour in the game mostly strategic?',
                               blank=True)
    comments = models.StringField(
        label='Do you have any final thoughts on the experiment or anything you would like to share with the experimenters?',
        blank=True)

    # Impulsiveness scale #
    def imp(x):
        return models.IntegerField(
            choices=[[1, 'Rarely/Never'], [2, 'Occasionally'],
                     [3, 'Often'], [4, 'Almost Always/Always']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    impa1r = imp('I am a careful thinker.')
    impn1r = imp('I plan trips well ahead of time.')
    impm1 = imp('I do things without thinking.')
    impa2r = imp('I concentrate easily.')
    impn2r = imp('I plan for job security.')
    impm2 = imp('I act “on impulse.”')
    impa3r = imp('I am self controlled.')
    impm3 = imp('I say things without thinking.')
    impa4 = imp('I don’t “pay attention.”')
    impm4 = imp('I act on the spur of the moment.')
    impn3r = imp('I plan tasks carefully.')
    impa5r = imp('I am a steady thinker.')
    impn4r = imp('I am future oriented.')


    # Self-Concept Clarity Scale #
    def scc(x):
        return models.IntegerField(
            choices=[[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Neither agree nor disagree'], [4, 'Agree'],
                     [5, 'Strongly agree']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    scc1r = scc('My beliefs about myself often conflict with one another.')
    scc2r = scc('On one day I might have one opinion of myself and on another day I might have a different opinion.')
    scc3r = scc('I spend a lot of time wondering about what kind of person I really am.')
    scc4r = scc('Sometimes I feel that I am not really the person that I appear to be.')
    scc5r = scc('When I think about the kind of person I have been in the past, I am not sure what I was really like.')
    scc6 = scc('I seldom experience conflict between the different aspects of my personality.')
    scc7r = scc('Sometimes I think I know other people better than I know myself.')
    scc8r = scc('My beliefs about myself seem to change very frequently.')
    scc9r = scc('If I were asked to describe my personality, my description might end up being different from one day to another day.')
    scc10r = scc('Even if I wanted to, I do not think I could tell someone what I am really like.')
    scc11 = scc('In general, I have a clear sense of who I am and what I am.')
    scc12r = scc('It is often hard for me to make up my mind about things because I do not really know what I want.')
    nfc = nfa('I make an effort to appear consistent to others.')


    # Social Desirability Scale #
    def sds(x):
        return models.IntegerField(
            choices=[[0, 'False'], [1, 'True']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    sds1 = sds('It is sometimes hard for me to go on with my work if I am not encouraged.')
    sds2 = sds('I sometimes feel resentful when I do not get my way.')
    sds3 = sds('On a few occasions, I have given up doing something because I though too little of my ability.')
    sds4 = sds('There have been times when I felt like rebelling against people in authority even though I knew they were right.')
    sds5 = sds('No matter who I am talking to, I am always a good listener.')
    sds6 = sds('There have been occasions when I took advantage of someone.')
    sds7 = sds('I am always willing to admit it when I make a mistake.')
    sds8 = sds('I sometimes try to get even rather than forgive and forget.')
    sds9 = sds('I am always polite, even to people who are disagreeable.')
    sds10 = sds('I have never been annoyed when people expressed ideas very different from my own.')
    sds11 = sds('There have been times when I was quite jealous of the good fortune of others.')
    sds12 = sds('I am sometimes irritated by people who ask favors of me.')
    sds13 = sds("I have never deliberately said something that would hurt someone's feelings.")
