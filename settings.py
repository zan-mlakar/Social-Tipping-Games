from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1,
    'participation_fee': 1,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'Experiment',
        'num_demo_participants': 3,
        'app_sequence': ['Intro', 'Game', 'Final'],
    },
    {
        'name': 'Test',
        'num_demo_participants': 3,
        'app_sequence': ['Game'],
    },
    {
        'name': 'Demographics',
        'num_demo_participants': 3,
        'app_sequence': ['Final'],
    }
]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ROOMS = [
]


ADMIN_USERNAME = 'username123'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'password456'


DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'rv#&dm$wqgi1-g8$2e*!y&4rm6u5n_su@#)#5gv+z3coe58e6c'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
