import os
import json


this_folder = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(this_folder, "info.json")


def get_info() -> dict:
    with open(config_path, "r+") as file:
        config = file.read()
        if not config:
            config = json.dumps({"RECENT_FILES": []})
            file.write(config)

    return json.loads(config)


def add_recent_file(path: str) -> None:
    info = get_info()
    recent_files = info["RECENT_FILES"]

    if recent_files.count(path) == 1:
        recent_files.remove(path)
    recent_files = [path] + recent_files

    if len(recent_files) > get_info()["RECENT_FILES_MAX_AMOUNT"]:
        recent_files = recent_files[:-1]

    info["RECENT_FILES"] = recent_files
    config_info = json.dumps(info)

    with open(config_path, "w") as file:
        file.write(config_info)


def remove_recent_file(path: str) -> None:
    info = get_info()
    recent_files = info["RECENT_FILES"]

    recent_files.remove(path)
    info["RECENT_FILES"] = recent_files

    config_info = json.dumps(info)
    with open(config_path, "w") as file:
        file.write(config_info)


def add_user_style(style_name: str, style: dict) -> None:
    info = get_info()
    user_styles = info["USER_STYLES"]

    if user_styles == {}:
        user_styles = dict()
        user_styles["New Style 1"] = style

    else:
        user_styles[style_name] = style

    info["USER_STYLES"] = user_styles
    config_info = json.dumps(info)

    with open(config_path, "w") as file:
        file.write(config_info)


def remove_user_style(style_name: str) -> None:
    info = get_info()
    user_styles = info["USER_STYLES"]

    user_styles.pop(style_name)
    info["USER_STYLES"] = user_styles

    config_info = json.dumps(info)
    with open(config_path, "w") as file:
        file.write(config_info)