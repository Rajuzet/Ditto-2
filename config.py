class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'your_database_uri'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///development.db'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///testing.db'

class ProductionConfig(Config):
    DATABASE_URI = 'postgresql://user:password@localhost/prod_db'