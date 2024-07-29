import os


def get_postgres_uri():
    host = "localhost"
    port = 5432
    password = "pgpwd4habr"
    user, db_name = "habrpguser", "habrdb"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"