import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class App:
    debug: bool
    name: str
    key: str
    choice_db: str


@dataclass
class Db:
    name: str
    user: str
    password: str
    host: str
    port: str
    url: str


@dataclass
class Redis:
    host: str
    port: str


@dataclass
class Email:
    host: str
    port: str
    tls: str
    ssl: str
    user: str
    password: str


@dataclass
class Config:
    app: App
    db: Db
    redis: Redis
    email: Email


def load_config(path:str = None) -> Config:
    if path:
        load_dotenv(path)
    else:
        load_dotenv()
    debug = True if os.getenv("DEBUG").lower() == 'true' else False
    url = os.getenv("DOMAIN_NAME")
    key = os.getenv("SECRET_KEY")
    choice_db = os.getenv("CHOICE_DB")

    db_user = os.getenv("MYSQL_USER")
    db_password = os.getenv("MYSQL_PASSWORD")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("MYSQL_DATABASE")
    db_host = os.getenv("DB_HOST")
    db_url = f"mysql://{db_user}:{db_password}@{db_host}/{db_name}?charset=utf8mb4"

    redis_host = os.getenv("REDIS_HOST")
    redis_port = os.getenv("REDIS_PORT")

    email_host = os.getenv("EMAIL_HOST")
    email_port = os.getenv("EMAIL_PORT")
    email_tls = os.getenv("EMAIL_USE_TLS")
    email_ssl = os.getenv("EMAIL_USE_SSL")
    email_user = os.getenv("EMAIL_HOST_USER")
    email_password = os.getenv("EMAIL_HOST_PASSWORD")

    return Config(db=Db(
        user=db_user,
        password=db_password,
        port=db_port,
        name=db_name,
        host=db_host,
        url=db_url
    ), app=App(
        debug=debug,
        name=url,
        key=key,
        choice_db=choice_db
    ), redis=Redis(
        host=redis_host,
        port=redis_port
    ), email=Email(
        host=email_host,
        port=email_port,
        tls=email_tls,
        ssl=email_ssl,
        user=email_user,
        password=email_password
    ))


config: Config = load_config()
