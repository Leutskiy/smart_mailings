import environ


@environ.config(prefix="APP")
class AppConfig():
    """
    Конфигурация приложения

    """

    env = environ.var()
    lang = environ.var(name="LANG")
    folder = environ.var(name="FOLDER")


cfg = environ.to_config(
    AppConfig,
    environ={
        "APP_ENV": "dev",
        "LANG": "Python",
        "FOLDER": "C:\\Bucket"})
