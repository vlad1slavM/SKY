from Yandex.services.files import *
from Yandex.DB.db import DataBase


def start(path: str) -> None:
    y = YandexFiles()
    y.get_files_list_from_cloud(path)


if __name__ == '__main__':
    y = YandexFiles()
    y.get_files_list_from_cloud('/test')
    database = DataBase()
    for key in y.files:
        file = y.files[key]
        database.insert(file.name, key, file.preview_link, file.md5, file.media_type)

