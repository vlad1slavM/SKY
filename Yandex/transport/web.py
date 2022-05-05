import requests
import dotenv
import os

dotenv.load_dotenv()

# TODO нужно будет добавить try except
# Также свои excepthions

YandexOAuth = os.environ.get('YANDEXOAUTH')


def get_list_files_dirs(path: str) -> dict:
    """Get list of files from Yandex DISK"""
    headers = {
        "Accept": "application/json",
        "Authorization": f"OAuth {YandexOAuth}"
    }
    params = {
        "path": path
    }
    list_files = requests.get("https://cloud-api.yandex.net/v1/disk/resources",
                              params=params,
                              headers=headers)
    return list_files.json()


def get_file_content(file_path: str) -> bytes:
    """Get content of file from Yandex DISK"""
    headers = {
        "Accept": "application/json",
        "Authorization": f"OAuth {YandexOAuth}"
    }
    params = {
        "path": file_path
    }

    download_link = requests.get("https://cloud-api.yandex.net/v1/disk/resources/download",
                                 params=params,
                                 headers=headers).json()['href']
    content = requests.get(download_link).content
    return content
