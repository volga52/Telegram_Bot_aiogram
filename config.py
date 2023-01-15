import ipaddress

from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr
    # для конфиденциальных данных, например, токена бота
    bot_container_name: str = 'bot_container_name'
    bot_image_name: str = 'botimage_name'
    bot_name: str
    bot_token: SecretStr
    admins: list
    use_redis: bool

    db_user: str = 'volga52'
    pg_password: str = 'examplePostgresPass'
    db_pass: str = 'pg_password'
    db_host: ipaddress.IPv4Address

    # Вложенный класс с дополнительными указаниями для настроек
    class Config:
        # Имя файла, откуда будут прочитаны данные
        # (относительно текущей рабочей директории)
        # env_file = '.env'
        env_file = '.env'
        # Кодировка читаемого файла
        env_file_encoding = 'utf-8'


if __name__ == '__main__':
    # При импорте файла сразу создастся
    # и провалидируется объект конфига,
    # который можно далее импортировать из разных мест
    config = Settings()

    for key, value in config:
        print(f'{key}: {value} <{type(value)}>')