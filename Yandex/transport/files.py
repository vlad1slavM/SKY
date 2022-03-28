import requests


# TODO нужно будет добавить try except
# Также свои excepthions

def get_list_files_dirs(path: str) -> dict:
    headers = {
        "Accept": "application/json",
        "Authorization": "OAuth AQAAAAAVWAlWAADLWyVJbHXmPEZSnL1L2TtLTrA"
    }
    params = {
        "path": path
    }
    list_files = requests.get("https://cloud-api.yandex.net/v1/disk/resources",
                              params=params,
                              headers=headers)
    return list_files.json()


def get_file_content(file_path: str) -> bytes:
    headers = {
        "Accept": "application/json",
        "Authorization": "OAuth AQAAAAAVWAlWAADLWyVJbHXmPEZSnL1L2TtLTrA"
    }
    params = {
        "path": file_path
    }

    download_link = requests.get("https://cloud-api.yandex.net/v1/disk/resources/download",
                                 params=params,
                                 headers=headers).json()['href']
    content = requests.get(download_link).content
    return content


