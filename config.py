import decouple


class Settings:
    CREDENTIALS_FILE = decouple.config("CREDENTIALS_FILE")
    SPREADSHEET_ID = decouple.config("SPREADSHEET_ID")
    POSTGRES_NAME = decouple.config("POSTGRES_NAME")
    POSTGRES_PASSWORD = decouple.config("POSTGRES_PASSWORD")
    POSTGRES_HOST = decouple.config("POSTGRES_HOST")
    POSTGRES_PORT = decouple.config("POSTGRES_PORT")
    POSTGRES_DB = decouple.config("POSTGRES_DB")
    GOOGLE_APPLICATION_CREDENTIALS = decouple.config("GOOGLE_APPLICATION_CREDENTIALS")
    CBRF_DAILY = decouple.config("CBRF_DAILY")
    TG_BOT_KEY = decouple.config("TG_BOT_KEY")
    REDIS_PORT = decouple.config("REDIS_PORT")
    REDIS_HOST = decouple.config("REDIS_HOST")
    SQLALCHEMY_DATABASE_URL = decouple.config("SQLALCHEMY_DATABASE_URL")
    DB_AUTOCOMMIT = False
    DB_AUTOFLUSH = False
