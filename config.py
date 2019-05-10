import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'LUCAS-AND-SUNNYS-SECRET-MESSAGE'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AUTHY_KEY = 'ed11f7a902a456c055bba7682089cd77'

    TWILIO_ACCOUNT_SID = 'ACb6b281dda3980d3aa32f5186f641d97a'
    TWILIO_AUTH_TOKEN = 'FjdEcBuTLbU9PtfV3qbyrimz8rbrn0jw'
    TWILIO_NUMBER = '16309312416'


